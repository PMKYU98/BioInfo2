def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()
        idx = int(f.readline().strip())

    return sInput, idx

def POSITION(lst):
    dicPos = {}
    for i in range(len(lst)):
        dicPos.setdefault(lst[i], [])
        dicPos[lst[i]].append(i)

    return dicPos

def MOVE_CURSOR(cursor, char, dicPosFirst, dicPosLast):
    idx = dicPosLast[char].index(cursor)
    return dicPosFirst[char][idx]

inputfile = '221122/221122_Q3_input2.txt'
sLast, idx = PARSE(inputfile)
sFirst = ''.join(sorted(sLast))

dicPosFirst, dicPosLast = POSITION(sFirst), POSITION(sLast)

answer = MOVE_CURSOR(idx, sLast[idx], dicPosFirst, dicPosLast)
print(answer)