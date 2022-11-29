def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        Threshold, Pseudocount = [float(x) for x in f.readline().strip().split(delimiter) if x != '']
        f.readline()
        Alphabet = [character for character in f.readline().strip().split(delimiter) if character != '']
        f.readline()

        lines = f.readlines()
        lstAlign = [line.strip() for line in lines]

        return Threshold, Pseudocount, Alphabet, lstAlign

def WRITE_ANSWER(States, Alphabet, lstTransProb, lstEmitProb):
    outputfile = '221129/221129_Q6_output.txt'
    States[0] = 'S'
    with open(outputfile, 'w') as f:
        f.write('\t' + '\t'.join(States) + '\n')
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

def IS_INSERTION(lstChar):
    global Threshold
    return lstChar.count('-') / len(lstChar) > Threshold

def SAY_IMD(lstIMDPrev, lstChar):
    temp = []

    if IS_INSERTION(lstChar):
        for i in range(len(lstChar)):
            if lstChar[i] == '-': temp.append('P' + lstIMDPrev[i][-1])
            else:
                if lstIMDPrev[i][0] == 'I': temp.append(lstIMDPrev[i])
                else: temp.append('I' + lstIMDPrev[i][-1])

        return True, temp
    else:
        for i in range(len(lstChar)):
            if lstChar[i] == '-': temp.append('D' + str(int(lstIMDPrev[i][-1]) + 1))
            else: temp.append('M' + str(int(lstIMDPrev[i][-1]) + 1))
    
        return False, temp

def TRANS_COUNT(lstIMD):
    dicTransNext = {}
    for i in range(len(lstIMD)):
        j = 0
        k = 0
        while j < len(lstIMD[i]) - 1:
            k = k + 1
            
            if lstIMD[i][k][0] == 'P':
                continue
            else:
                dicTransNext.setdefault(lstIMD[i][j], [])
                dicTransNext[lstIMD[i][j]].append(lstIMD[i][k])
                j = k
        
    return dicTransNext

def EMIT_COUNT(lstAlign, lstIMD):
    dicEmit = {}
    for idx in range(len(lstAlign)):
        seq = lstAlign[idx]
        IMD = lstIMD[idx][1:-1]
        for step in range(len(IMD)):
            state = IMD[step]
            if state[0] == 'I' or state[0] == 'M':
                dicEmit.setdefault(state, [])
                dicEmit[state].append(seq[step])

    return dicEmit

def CALC_TRANS(lstAlign):
    lstIMD = [['S0'] for _ in range(len(lstAlign))]
    temp = ['S0'] * len(lstAlign)
    insertion = 0
    for i in range(len(lstAlign[0])):
        inserted, temp = SAY_IMD(temp, [sequence[i] for sequence in lstAlign])
        for j in range(len(temp)):
            lstIMD[j].append(temp[j])
        if inserted: insertion += 1

    for j in range(len(temp)):
            lstIMD[j].append('E')

    dicTransNext = TRANS_COUNT(lstIMD)
    
    States = ['S0']
    for step in range(len(lstAlign[0]) - insertion):
        States.append('I' + str(step))
        States.append('M' + str(step + 1))
        States.append('D' + str(step + 1))
    States.append('I' + str(step + 1))
    States.append('E')

    lstTransProb = []
    for l in States:
        if l == 'E':
            lstTransProb.append([0.0] * len(States))
        elif l in dicTransNext:
            row = []
            count = len(dicTransNext[l])
            nexts = dicTransNext[l]

            for j in States:
                row.append(nexts.count(j) / count)
            lstTransProb.append(row)
        else:
            lstTransProb.append([0.0] * len(States))
            
    return States, lstIMD, lstTransProb

def CALC_EMIT(Alphabet, States, lstIMD, lstAlign):
    dicEmit = EMIT_COUNT(lstAlign, lstIMD)

    lstEmitProb = []
    for l in States:
        if l in dicEmit:
            row = []
            count = len(dicEmit[l])
            nexts = dicEmit[l]

            for j in Alphabet:
                row.append(nexts.count(j) / count)
            lstEmitProb.append(row)
        else:
            lstEmitProb.append([0] * len(Alphabet))

    return lstEmitProb

def PSEUDOCOUNT(States, Alphabet, Pseudocount, lstTransProb, lstEmitProb):
    lstEmitProbNew = []
    for i in range(len(States)):
        if States[i][0] in ['S', 'D', 'E']: lstEmitProbNew.append([0] * len(Alphabet))
        else:
            sum_prob = sum(lstEmitProb[i]) + Pseudocount * len(Alphabet)
            temp = [(prob + Pseudocount) / sum_prob for prob in lstEmitProb[i]]
            lstEmitProbNew.append(temp)

    lstTransProbNew = []
    final = States[-2][-1]
    for i in range(len(States)):
        if States[i] == 'E':
            lstTransProbNew.append(lstTransProb[i])
            return lstEmitProbNew, lstTransProbNew

        num = States[i][1]
        if num == final:
            st = 3 * int(num) + 1
            ed = 3 * int(num) + 2
            sum_prob = sum(lstTransProb[i][st:ed+1]) + Pseudocount * 2
            temp = lstTransProb[i]
            temp[st] = (lstTransProb[i][st] + Pseudocount) / sum_prob
            temp[st+1] = (lstTransProb[i][st+1] + Pseudocount) / sum_prob
            
        else:
            st = 3 * int(num) + 1
            ed = 3 * int(num) + 3
            sum_prob = sum(lstTransProb[i][st:ed+1]) + Pseudocount * 3
            temp = lstTransProb[i]
            temp[st] = (lstTransProb[i][st] + Pseudocount) / sum_prob
            temp[st+1] = (lstTransProb[i][st+1] + Pseudocount) / sum_prob
            temp[st+2] = (lstTransProb[i][st+2] + Pseudocount) / sum_prob

        lstTransProbNew.append(temp)


inputfile = '221129/221129_Q6_input1.txt'
Threshold, Pseudocount, Alphabet, lstAlign = PARSE(inputfile)
States, lstIMD, lstTransProb = CALC_TRANS(lstAlign)

lstEmitProb = CALC_EMIT(Alphabet, States, lstIMD, lstAlign)
lstEmitProb, lstTransProb = PSEUDOCOUNT(States, Alphabet, Pseudocount, lstTransProb, lstEmitProb)
WRITE_ANSWER(States, Alphabet, lstTransProb, lstEmitProb)