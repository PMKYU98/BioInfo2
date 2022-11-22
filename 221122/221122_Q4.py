def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()
        lstPattern = f.readline().strip().split(' ')

    return sInput, lstPattern

def WRITE_OUTPUT(sOutput):
    outputfile = '221122/221122_Q4_output.txt'
    with open(outputfile, 'w') as f:
        f.write(sOutput)

    return

def POSITION(lst):
    dicPos = {}
    for i in range(len(lst)):
        dicPos.setdefault(lst[i], [])
        dicPos[lst[i]].append(i)

    return dicPos

def LAST_TO_FIRST(posLast, char, dicPosFirst, dicPosLast):
    idx = dicPosLast[char].index(posLast)
    return dicPosFirst[char][idx]

def POS_BETWEEN(top, bottom, positions):
    temp = [pos for pos in positions if top <= pos <= bottom]
    return temp[0], temp[-1]
    
def BWMATCHING(sFirst, sLast, pattern):
    dicPosFirst, dicPosLast = POSITION(sFirst), POSITION(sLast)
    top, bottom = 0, len(sLast) - 1

    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            if symbol in sLast[top:bottom+1]:
                idx_top, idx_btm = POS_BETWEEN(top, bottom, dicPosLast[symbol])

                top = LAST_TO_FIRST(idx_top, symbol, dicPosFirst, dicPosLast)
                bottom = LAST_TO_FIRST(idx_btm, symbol, dicPosFirst, dicPosLast)
            else:
                return 0
        else:
            return bottom - top + 1

inputfile = '221122/221122_Q4_input1.txt'
sLast, lstPattern = PARSE(inputfile)
sFirst = ''.join(sorted(sLast))
answer = [str(BWMATCHING(sFirst, sLast, pattern)) for pattern in lstPattern]
WRITE_OUTPUT(' '.join(answer))