def PARSE(inputfile):
    fInput = open(inputfile, 'r')
    inputdata = fInput.readlines()
    fInput.close()

    sequence = inputdata[0].strip()
    alphabet = inputdata[2].split()
    alphabet2i = {a: i for i, a in enumerate(alphabet)}

    states = inputdata[4].split()
    states2i = {a: i for i, a in enumerate(states)}

    temp_tr = inputdata[7:7+len(states)]
    trprob = [[float(x) for x in l.split()[1:]] for l in temp_tr]

    temp_em = inputdata[9+len(states):9+2*len(states)]
    emprob = [[float(x) for x in l.split()[1:]] for l in temp_em]

    return sequence, alphabet2i, states2i, trprob, emprob, states, alphabet

def WEIGHT(prev, state, step):
    global sequence, alphabet, states, alphabet2i, states2i, trprob, emprob

    if step == 0:
        return emprob[state][alphabet2i[sequence[step]]]
    else:
        return trprob[prev][state] * emprob[state][alphabet2i[sequence[step]]]

def SCORE(state, step, lstScores):
    global states

    if step == 0:
        return 1 / len(states) * WEIGHT(-1, state, step)
    else:
        temp = 0
        for prev in range(len(states)):
            temp += lstScores[step-1][prev] * WEIGHT(prev, state, step)

        return temp

def FORWARD(k, i):
    global sequence, states

    lstScores = []
    if i == 0: return 1/len(states) * WEIGHT('', k, i)
    else:
        temp = []
        for step in range(i):
            SCORE

inputfile = '221206/221206_Q4_input1.txt'
sequence, alphabet2i, states2i, trprob, emprob, states, alphabet = PARSE(inputfile)
