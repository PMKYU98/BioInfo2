from math import log10

def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        sString = f.readline().strip()
        f.readline()
        Alphabet = [character for character in f.readline().strip().split(delimiter) if character != '']
        f.readline()
        States = [character for character in f.readline().strip().split(delimiter) if character != '']
        f.readline()
        f.readline()

        lstTransProb = []
        lines = f.readlines()
        for l in lines[:len(States)]:
            line = l.strip().split(delimiter)[1:]
            lstTransProb.append([float(prob) for prob in line if prob != ''])

        lstEmitProb = []
        for l in lines[len(States)+2:]:
            line = l.strip().split(delimiter)[1:]
            lstEmitProb.append([float(prob) for prob in line if prob != ''])

        return sString, Alphabet, States, lstTransProb, lstEmitProb

def LOG_WEIGHT(l, k, i):
    global sString, Alphabet, States, lstTransProb, lstEmitProb

    if i == 0:
        return log10(lstEmitProb[States.index(k)][Alphabet.index(sString[i])])
    else:
        return log10(lstTransProb[States.index(l)][States.index(k)]) \
            + log10(lstEmitProb[States.index(k)][Alphabet.index(sString[i])])

def LOG_SCORE(k, i, lstScores):
    global States

    if i == 0:
        return 'O', LOG_WEIGHT('', k, i)
    else:
        for j in range(len(States)):
            temp = lstScores[i-1][j] + LOG_WEIGHT(States[j], k, i)
            if j == 0: temp_idx, temp_max = 0, temp
            else:
                if temp > temp_max:
                    temp_idx, temp_max = j, temp

        return States[temp_idx], temp_max

def VITERBI():
    global sString

    lstScores = []
    lstBacktrack = []
    for i in range(len(sString)):
        tempScores = []
        tempBacktrack = []
        for j in range(len(States)):
            state, score = LOG_SCORE(States[j], i, lstScores)
            tempScores.append(score)
            tempBacktrack.append(state)

        lstScores.append(tempScores)
        lstBacktrack.append(tempBacktrack)

    return lstScores, lstBacktrack

def BACKTRACK(lstScores, lstBacktrack):
    global States
    
    max_score = max(lstScores[-1])
    max_state = lstScores[-1].index(max_score)
    backtrack = [States[max_state]]

    for temp in reversed(lstBacktrack):
        prev = temp[max_state]
        if prev == 'O': break
        backtrack.append(prev)
        max_state = States.index(prev)

    return ''.join(reversed(backtrack))
        

inputfile = '221129/221129_Q3_input2.txt'
sString, Alphabet, States, lstTransProb, lstEmitProb = PARSE(inputfile, '\t')

lstScores, lstBacktrack = VITERBI()
backtrack = BACKTRACK(lstScores, lstBacktrack)
print(backtrack)