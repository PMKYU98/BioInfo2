import numpy as np
import pandas as pd
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

    return sequence, alphabet2i, trprob, emprob, states, alphabet

def zerocol(trprob, states):
    nmatches = sum([s[0] == 'M' for s in states])
    initprob = [1]

    # Generate the first column for initial deletions
    for k in range(1, nmatches + 1):
        initprob.append(initprob[-1] * trprob[3*(k-1),3*k])

    return initprob

def firstcol(observation, initprob, trprob, emprob, states):
    state2i = {stname: i for i, stname in enumerate(states)}
    _states = states[1:-1]
    nstates = len(_states)
    obslen = len(observation)

    probprod = np.zeros([nstates, obslen], dtype=np.float64)
    back1 = np.zeros([nstates, obslen], dtype=np.int16)
    back2 = np.zeros([nstates, obslen], dtype=np.int16)

    j, obs = 0, observation[0]
    for s in range(nstates):
        state = _states[s]
        k = int(state[1])
        if _states[s][0] == 'I': 
            probprod[s, 0] = initprob[k] * trprob[state2i[states[3*k]], state2i[state]] * emprob[s+1, obs]
            back1[s, 0], back2[s, 0] = (-1, k)

        elif _states[s][0] == 'M': 
            probprod[s, 0] = initprob[k-1] * trprob[state2i[states[3*(k-1)]], state2i[state]] * emprob[s+1, obs]
            back1[s, 0], back2[s, 0] = (-1, k-1)
        elif _states[s][0] == 'D': 
            if k > 1:
                incoming_prob = [probprod[s-4, 0] * trprob[s - 3, s + 1],
                    probprod[s-3, 0] * trprob[s - 2, s + 1],
                    probprod[s-2, 0] * trprob[s - 1, s + 1]]
                l = np.argmax(incoming_prob)
                probprod[s, j] = incoming_prob[l]
                back1[s, 0], back2[s, 0] = (0, s - 4 + l)
            else:
                probprod[s, 0] = probprod[s-2, 0] * trprob[s - 1, s + 1]
                back1[s, 0], back2[s, 0] = (0, s - 2)
    
    return probprod, back1, back2

def viterbi(observation, trprob, emprob, states):
    initprob = zerocol(trprob, states)

    probprod, back1, back2 = firstcol(observation, initprob, trprob, emprob, states)
    print(probprod)

    state2i = {stname: i for i, stname in enumerate(states)}
    _states = states[1:-1]
    nstates = len(_states)
    
    for j, obs in enumerate(observation[1:], 1):
        for s in range(nstates):
            state = _states[s]
            k = int(state[1])

            if _states[s][0] == 'I':
                if k == 0:
                    probprod[s, j] = probprod[s, j-1] * trprob[state2i[states[3*k]], state2i[state]] * emprob[s+1, obs]
                    back1[s, j], back2[s, j] = (j-1, k)
                else: 
                    incoming_prob = [probprod[s-2, j-1] * trprob[s - 1, s + 1] * emprob[s+1, obs],
                    probprod[s-1, j-1] * trprob[s, s + 1] * emprob[s+1, obs],
                    probprod[s, j-1] * trprob[s + 1, s + 1] * emprob[s+1, obs]]
                    l = np.argmax(incoming_prob)
                    probprod[s, j] = incoming_prob[l]
                    back1[s, j], back2[s, j] = (j-1, s - 2 + l)
            elif _states[s][0] == 'M':
                if k == 1:
                    probprod[s, j] = probprod[s-1, j-1] * trprob[state2i['I0'], state2i[state]] * emprob[s+1, obs]
                    back1[s, j], back2[s, j] = (j-1, s-1)
                else: 
                    incoming_prob = [probprod[s-3, j-1] * trprob[s - 2, s + 1] * emprob[s+1, obs],
                    probprod[s-2, j-1] * trprob[s-1, s + 1] * emprob[s+1, obs],
                    probprod[s-1, j-1] * trprob[s, s + 1] * emprob[s+1, obs]]
                    l = np.argmax(incoming_prob)
                    probprod[s, j] = incoming_prob[l]
                    back1[s, j], back2[s, j] = (j-1, s - 3 + l)
            elif _states[s][0] == 'D': 
                if k > 1:
                    incoming_prob = [probprod[s-4, 0] * trprob[s - 3, s + 1],
                        probprod[s-3, 0] * trprob[s - 2, s + 1],
                        probprod[s-2, 0] * trprob[s - 1, s + 1]]
                    l = np.argmax(incoming_prob)
                    probprod[s, j] = incoming_prob[l]
                    back1[s, j], back2[s, j] = (j, s - 4 + l)
                else:
                    probprod[s, 0] = probprod[s-2, 0] * trprob[s - 1, s + 1]
                    back1[s, j], back2[s, j] = (j, s - 2)
    
    best_path = []
    k = len(_states) - 3 + np.argmax(probprod[:, -1][-3:])
    j = len(observation) - 1
    
    while j >= 0:
        print(j, k)
        best_path.append(k + 1)
        k = back2[k, j]
        j = back1[k, j]

    while k > 0:
        best_path.append(k * 3)
        k -= 1

    return best_path[::-1]
    


inputfile = '221206/221206_Q1_input2.txt'
sequence, alphabet2i, trprob, emprob, states, alphabet = PARSE(inputfile)
observation = [alphabet2i[s] for s in sequence]

import pandas as pd
trprob_tbl = pd.DataFrame(trprob, index=states, columns=states)
emprob_tbl = pd.DataFrame(emprob, index=states, columns=alphabet)

decoded_states = viterbi(observation, trprob, emprob, states)

print(' '.join([states[i] for i in decoded_states]))