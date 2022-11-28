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

inputfile = '221129/221129_Q3_input1.txt'
sString, Alphabet, States, lstTransProb, lstEmitProb = PARSE(inputfile)
print(sString)
print(Alphabet)
print(States)
print(lstTransProb)
print(lstEmitProb)