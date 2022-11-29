def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        sString = f.readline().strip()
        f.readline()
        Alphabet = [character for character in f.readline().strip().split(delimiter) if character != '']
        f.readline()
        sEmission = f.readline().strip()
        f.readline()
        States = [character for character in f.readline().strip().split(delimiter) if character != '']
        f.readline()
        f.readline()

        lstProb = []
        lines = f.readlines()
        for l in lines:
            line = l.strip().split(delimiter)[1:]
            lstProb.append([float(prob) for prob in line if prob != ''])

    return sString, Alphabet, sEmission, States, lstProb

def PATH_PROB(sString, Alphabet, sEmission, States, lstProb):
    prob = 1
    for level in range(len(sString)):
        prob *= lstProb[States.index(sEmission[level])][Alphabet.index(sString[level])]

    return prob


inputfile = '221129/221129_Q2_input1.txt'
sString, Alphabet, sEmission, States, lstProb = PARSE(inputfile)
print(PATH_PROB(sString, Alphabet, sEmission, States ,lstProb))
