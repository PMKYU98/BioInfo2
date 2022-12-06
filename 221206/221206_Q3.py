import numpy as np
from math import log10

def PARSE(inputfile):
    fInput = open(inputfile, 'r')
    inputdata = fInput.readlines()
    fInput.close()

    iter = int(inputdata[0].strip())
    sequence = inputdata[2].strip()
    alphabet = inputdata[4].split()
    alphabet2i = {a: i for i, a in enumerate(alphabet)}

    states = inputdata[6].split()
    states2i = {a: i for i, a in enumerate(states)}

    temp_tr = inputdata[9:9+len(states)]
    trprob = [[float(x) for x in l.split()[1:]] for l in temp_tr]

    temp_em = inputdata[11+len(states):11+2*len(states)]
    emprob = [[float(x) for x in l.split()[1:]] for l in temp_em]

    return iter, sequence, alphabet2i, states2i, trprob, emprob, states, alphabet

def phmm_topological_order(obslen, states):
    # Generate toplogical ordering for the remaining columns
    for i in range(1, obslen + 1):
        for k in range(len(states)):
            yield (i, k)

    # Generate 'E' state
    yield (obslen+1, len(states)+1)

def backtrack(obslen, dicBack):
    answer = []
    step = 0

    for step, state in dicBack:
        if step == obslen + 1: break
    
    while step > 0:
        answer.append(state)
        step, state = dicBack[(step, state)]

    return list(reversed(answer[1:]))

def viterbi(observation, trprob, emprob, states):
    states2i = {state: i for i, state in enumerate(states)}
    dicProb = {(0, len(states)): 0}
    dicBack = {}

    for step, state in phmm_topological_order(len(observation), states):
        if step == len(observation) + 1:
            lstProb = [dicProb[(step-1, states2i[prev])] for prev in states]
            k = np.argmax(lstProb)
            dicBack[(step, state)] = (step-1, k)
            break

        obs = observation[step - 1]
        if step == 1:
            dicProb[(step, state)] = emprob[state][obs]
            dicBack[(step, state)] = (0, len(states))
        else:
            lstProb = [dicProb[(step-1, states2i[prev])] * trprob[states2i[prev]][state] * emprob[state][obs] for prev in states]
            k = np.argmax(lstProb)
            dicProb[(step, state)] = lstProb[k]
            dicBack[(step, state)] = (step-1, k)

    answer = backtrack(len(observation), dicBack)
    return ''.join([states[i] for i in answer])

def EXPLORE(String, Path, States):
    dicEmission = {state: [] for state in States}
    dicTransition = {state: [] for state in States}

    for i in range(len(String) - 1):
        state = Path[i]
        emit = String[i]
        nextstate = Path[i+1]

        dicEmission[state].append(emit)
        dicTransition[state].append(nextstate)

    dicEmission[Path[-1]].append(String[-1])
    return dicEmission, dicTransition

def CALCULATE(dicTransition, dicEmission, States, Alphabet):
    lstTransProb = []
    for l in States:
        if len(dicTransition[l]) == 0:
            lstTransProb.append([1 / len(States) for _ in States])
            continue
        lstTransProb.append([dicTransition[l].count(k) / len(dicTransition[l]) for k in States])

    lstEmitProb = []
    for l in States:
        if len(dicEmission[l]) == 0:
            lstEmitProb.append([1 / len(Alphabet) for _ in Alphabet])
            continue
        lstEmitProb.append([dicEmission[l].count(c) / len(dicEmission[l]) for c in Alphabet])

    return lstTransProb, lstEmitProb

def VITERBI_LEARNING(iter, sequence, observation, trprob, emprob, states, alphabet):
    for _ in range(iter):
        path = viterbi(observation, trprob, emprob, states)

        dicEmission, dicTransition = EXPLORE(sequence, path, states)
        trprob, emprob = CALCULATE(dicTransition, dicEmission, states, alphabet)

    return trprob, emprob

inputfile = '221206/221206_Q3_input1.txt'
iter, sequence, alphabet2i, states2i, trprob, emprob, states, alphabet = PARSE(inputfile)
observation = [alphabet2i[s] for s in sequence]

trprob, emprob = VITERBI_LEARNING(iter, sequence, observation, trprob, emprob, states, alphabet)
print(trprob)
print(emprob)