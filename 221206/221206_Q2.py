def PARSE(fInput):
    with open(fInput, 'r') as f:
        String = f.readline().strip()
        f.readline()
        Alphabet = [character for character in f.readline().strip().split() if character != '']
        f.readline()
        Path = f.readline().strip()
        f.readline()
        States = [character for character in f.readline().strip().split() if character != '']

        return String, Alphabet, Path, States

def WRITE_ANSWER(States, Alphabet, lstTransProb, lstEmitProb):
    outputfile = '221206/221206_Q2_output.txt'
    with open(outputfile, 'w') as f:
        f.write('\t'.join(States) + '\n')
        for i in range(len(lstTransProb)):
            l = [States[i]]
            l.extend(['%.3f' % x for x in lstTransProb[i]])
            f.write('\t'.join(l) + '\n')
        
        f.write('--------\n')
        f.write('\t' + '\t'.join(Alphabet) + '\n')
        for i in range(len(lstEmitProb)):
            l = [States[i]]
            l.extend(['%.3f' % x for x in lstEmitProb[i]])
            f.write('\t'.join(l) + '\n')

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

inputfile = '221206/221206_Q2_input1.txt'
String, Alphabet, Path, States = PARSE(inputfile)
dicEmission, dicTransition = EXPLORE(String, Path, States)
lstTransProb, lstEmitProb = CALCULATE(dicTransition, dicEmission, States, Alphabet)
WRITE_ANSWER(States, Alphabet, lstTransProb, lstEmitProb)