def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        sPath = f.readline().strip()
        f.readline()
        States = [state for state in f.readline().strip().split(delimiter) if state != '']
        f.readline()
        f.readline()

        lstProb = []
        lines = f.readlines()
        for l in lines:
            line = l.strip().split(delimiter)[1:]
            lstProb.append([float(prob) for prob in line if prob != ''])

    return sPath, States, lstProb

def PATH_PROB(sPath, States, lstProb):
    prob = 1 / len(States)
    curr = sPath[0]

    for next in sPath[1:]:
        temp = lstProb[States.index(curr)][States.index(next)]
        prob *= temp
        
        curr = next

    return prob


inputfile = '221129/221129_Q1_input1.txt'
sPath, States, lstProb = PARSE(inputfile)
print(PATH_PROB(sPath, States, lstProb))