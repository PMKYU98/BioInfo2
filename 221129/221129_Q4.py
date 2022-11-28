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

def WEIGHT(l, k, i):
    global sString, Alphabet, States, lstTransProb, lstEmitProb

    if i == 0:
        return lstEmitProb[States.index(k)][Alphabet.index(sString[i])]
    else:
        return lstTransProb[States.index(l)][States.index(k)] \
            * lstEmitProb[States.index(k)][Alphabet.index(sString[i])]

def SCORE(k, i, lstScores):
    global States

    if i == 0:
        return 1 / len(States) * WEIGHT('', k, i)
    else:
        temp = 0
        for j in range(len(States)):
            temp += lstScores[i-1][j] * WEIGHT(States[j], k, i)

        return temp

def FORWARD():
    global sString

    lstScores = []
    for i in range(len(sString)):
        tempScores = []
        for j in range(len(States)):
            tempScores.append(SCORE(States[j], i, lstScores))

        lstScores.append(tempScores)

    return lstScores

inputfile = '221129/221129_Q4_input1.txt'
sString, Alphabet, States, lstTransProb, lstEmitProb = PARSE(inputfile)

lstScores = FORWARD()
print(sum(lstScores[-1]))