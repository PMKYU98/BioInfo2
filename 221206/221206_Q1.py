import numpy as np
import pandas as pd

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
        if state[0] in 'SE':
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
    yield (obslen, state2i['E'])

def viterbi(observation, initprob, trprob, emprob):
    nstates = len(initprob)

    probprod = np.zeros([nstates, len(observation)], dtype=np.float64)
    backtrack = np.zeros([nstates, len(observation)], dtype=np.int16)

    probprod[:, 0] = emprob[:, observation[0]] * initprob

    for j, obs in enumerate(observation[1:], 1):
        for s in range(nstates):
            k = np.argmax(probprod[:, j-1] * trprob[:, s] * emprob[s, obs])
            probprod[s, j] = probprod[k, j-1] * trprob[k, s] * emprob[s, obs]
            backtrack[s, j] = k

    best_path = []
    k = np.argmax(probprod[:, -1])
    for j in range(len(observation) - 1, -1, -1):
        best_path.append(k)
        k = backtrack[k, j]
    return best_path[::-1]


inputfile = '221206/221206_Q1_input1.txt'
sequence, alphabet2i, trprob, emprob, states = PARSE(inputfile)
observation = [alphabet2i[s] for s in sequence]
initprob = [1 / len(states)] * len(states)

decoded_states = viterbi(observation, initprob, trprob, emprob)
print(' '.join([states[i] for i in decoded_states]))

obslen = len(observation)
for state in phmm_topological_order(obslen, states):
    print(state)