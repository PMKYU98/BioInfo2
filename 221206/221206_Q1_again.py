import numpy as np
from math import log10

def construct_profile_hmm(threshold, alphabet, msa, pseudocount=0.01):
    # Assign the states with available alignments over the threshold
    matchno = 0
    statemap = {}
    for i in range(len(msa[0])):
        unavailable = sum([seq[i] == '-' for seq in msa])
        if unavailable / len(msa) < threshold:
            matchno += 1
            statemap[i] = f'M{matchno}'
        else:
            statemap[i] = f'I{matchno}'

    states = ['S', 'I0'] + [
        f'{op}{i}' for i in range(1, matchno+1) for op in 'MDI'] + ['E']
    state2i = {s: i for i, s in enumerate(states)}
    sym2i = {s: i for i, s in enumerate(alphabet)}

    trcnt = np.zeros((len(states), len(states)), dtype=int)
    emcnt = np.zeros((len(states), len(alphabet)), dtype=int)

    for seq in msa:
        calls = ['S']
        for i, sym in enumerate(seq):
            state = statemap[i]
            if sym != '-':
                emcnt[state2i[state], sym2i[sym]] += 1
                statecall = state
            elif state[0] == 'M':
                statecall = 'D' + state[1:]
            else:
                continue

            calls.append(statecall)

        calls.append('E')

        for a, b in zip(calls, calls[1:]):
            trcnt[state2i[a], state2i[b]] += 1

    trprob = trcnt / trcnt.sum(axis=1).clip(1)[:, np.newaxis]
    emprob = emcnt / emcnt.sum(axis=1).clip(1)[:, np.newaxis]

    # Add pseudocounts
    for state in states:
        if state[0] == 'E':
            continue
        elif state[0] == 'S':
            outgoing = ['I0', 'M1', 'D1']
            outgoing = [state2i[s] for s in outgoing]
            probspace = state2i[state], outgoing
            newprob = trprob[probspace] + pseudocount
            trprob[probspace] = newprob / newprob.sum()
            continue

        snum = int(state[1:])
        snext = snum + 1

        # Add pseudocounts to transition probabilities
        if snum == matchno:
            outgoing = [f'I{snum}', 'E']
        else:
            outgoing = [f'I{snum}', f'M{snext}', f'D{snext}']

        outgoing = [state2i[s] for s in outgoing]
        probspace = state2i[state], outgoing
        newprob = trprob[probspace] + pseudocount
        trprob[probspace] = newprob / newprob.sum()

        # Add pseudocounts to emission probabilities
        if state[0] == 'D':
            continue

        si = state2i[state]
        newprob = emprob[si] + pseudocount
        emprob[si] = newprob / newprob.sum()

    return trprob, emprob, states

def PARSE(inputfile):
    fInput = open(inputfile, 'r')
    inputdata = fInput.readlines()
    fInput.close()

    sequence = inputdata[0].strip()

    secondline = inputdata[2].strip().split()
    threshold = float(secondline[0])
    pseudocount = float(secondline[1])

    alphabet = inputdata[4].split()
    alphabet2i = {a: i for i, a in enumerate(alphabet)}

    msa = [l.strip() for l in inputdata[6:]]

    trprob, emprob, states = construct_profile_hmm(threshold, alphabet, msa, pseudocount)

    return sequence, alphabet2i, trprob, emprob, states

def phmm_topological_order(obslen, states):
    state2i = {stname: i for i, stname in enumerate(states)}
    nmatches = sum([s[0] == 'M' for s in states])

    # Generate the first column for initial deletions
    for k in range(1, nmatches + 1):
        yield (0, state2i[f'D{k}'])

    # Generate toplogical ordering for the remaining columns
    for i in range(1, obslen + 1):
        for k in range(1, len(states) - 1): # except S, E
            yield (i, k)

    # Generate 'E' state
    yield (obslen+1, state2i['E'])

def backtrack(obslen, dicBack):
    answer = []
    for step, state in dicBack:
        if step == obslen + 1: break
    
    while step > 0:
        answer.append(state)
        step, state = dicBack[(step, state)]

    return reversed(answer[1:])

def viterbi(observation, trprob, emprob, states):
    dicProb = {(0, 0): 0}
    dicBack = {}

    for step, state in phmm_topological_order(len(observation), states):
        if step == 0: dicProb[(step, state)] = dicProb[(0, (state/3 - 1) * 3)] + log10(trprob[state - 3, state])
        elif step == 1:
            obs = observation[step - 1]
            if state % 3 == 1:   # I
                dicProb[(step, state)] = dicProb[(0, state-1)] + log10(trprob[state - 1, state]) + log10(emprob[state, obs])
                dicBack[(step, state)] = (0, state-1)
            if state % 3 == 2:   # M
                dicProb[(step, state)] = dicProb[(0, state-2)] + log10(trprob[state - 2, state]) + log10(emprob[state, obs])
                dicBack[(step, state)] = (0, state-2)
            if state % 3 == 0:   # D
                if state == 3:
                    dicProb[(step, state)] = dicProb[(1, state-2)] + log10(trprob[state - 2, state])
                    dicBack[(step, state)] = (1, state-2)
                else:
                    #MDI
                    lstProb = [dicProb[(1, state-4)] + log10(trprob[state - 4, state]),
                    dicProb[(1, state-3)] + log10(trprob[state - 3, state]),
                    dicProb[(1, state-2)] + log10(trprob[state - 2, state])]
                    k = np.argmax(lstProb)
                    dicProb[(step, state)] = lstProb[k]
                    dicBack[(step, state)] = (1, state-4+k)
        elif step == len(observation) + 1:
            lstProb = [dicProb[(step-1, state-3)], dicProb[(step-1, state-2)], dicProb[(step-1, state-1)]]
            k = np.argmax(lstProb)
            dicProb[(step, state)] = lstProb[k]
            dicBack[(step, state)] = (step - 1, state-3+k)
        else:
            obs = observation[step - 1]
            if state % 3 == 1:   # I
                if state == 1:
                    dicProb[(step, state)] = dicProb[(step-1, state)] + log10(trprob[state, state]) + log10(emprob[state, obs])
                    dicBack[(step, state)] = (step-1, state)
                else:
                    #MDI
                    lstProb = [dicProb[(step-1, state-2)] + log10(trprob[state - 2, state]) + log10(emprob[state, obs]),
                    dicProb[(step-1, state-1)] + log10(trprob[state - 1, state]) + log10(emprob[state, obs]),
                    dicProb[(step-1, state)] + log10(trprob[state, state]) + log10(emprob[state, obs])]
                    k = np.argmax(lstProb)
                    dicProb[(step, state)] = lstProb[k]
                    dicBack[(step, state)] = (step-1, state-2+k)
            if state % 3 == 2:   # M
                if state == 2:
                    dicProb[(step, state)] = dicProb[(step-1, state-1)] + log10(trprob[state - 2, state]) + log10(emprob[state, obs])
                    dicBack[(step, state)] = (step-1, state-1)
                else:
                    #MDI
                    lstProb = [dicProb[(step-1, state-3)] + log10(trprob[state - 3, state]) + log10(emprob[state, obs]),
                    dicProb[(step-1, state-2)] + log10(trprob[state - 2, state]) + log10(emprob[state, obs]),
                    dicProb[(step-1, state-1)] + log10(trprob[state - 1, state]) + log10(emprob[state, obs])]
                    k = np.argmax(lstProb)
                    dicProb[(step, state)] = lstProb[k]
                    dicBack[(step, state)] = (step-1, state-3+k)
            if state % 3 == 0:   # D
                if state == 3:
                    dicProb[(step, state)] = dicProb[(step, state-2)] + log10(trprob[state - 2, state])
                    dicBack[(step, state)] = (step, state-2)
                else:
                    #MDI
                    lstProb = [dicProb[(step, state-4)] + log10(trprob[state - 4, state]),
                    dicProb[(step, state-3)] + log10(trprob[state - 3, state]),
                    dicProb[(step, state-2)] + log10(trprob[state - 2, state])]
                    k = np.argmax(lstProb)
                    dicProb[(step, state)] = lstProb[k]
                    dicBack[(step, state)] = (step, state-4+k)

    return backtrack(len(observation), dicBack)


inputfile = '221206/221206_Q1_input3.txt'
sequence, alphabet2i, trprob, emprob, states = PARSE(inputfile)
observation = [alphabet2i[s] for s in sequence]

decoded_states = viterbi(observation, trprob, emprob, states)
print(' '.join([states[i] for i in decoded_states]))