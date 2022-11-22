def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()

    return sInput

def WRITE_OUTPUT(sOutput):
    outputfile = '221122/221122_Q2_output.txt'
    with open(outputfile, 'w') as f:
        f.write(sOutput)

    return

def POSITION(lst):
    dicPos = {}
    for i in range(len(lst)):
        dicPos.setdefault(lst[i], [])
        dicPos[lst[i]].append(i)

    return dicPos

def MOVE_CURSOR(cursor, char, dicPosFirst, dicPosLast):
    idx = dicPosLast[char].index(cursor)
    return dicPosFirst[char][idx]

def INVERSION(sInput):
    sFirst, sLast = ''.join(sorted(sInput)), sInput

    dicPosFirst, dicPosLast = POSITION(sFirst), POSITION(sLast)
    temp = ['$']
    cursor = 0

    while len(temp) < len(sFirst):
        temp.append(sLast[cursor])
        cursor = MOVE_CURSOR(cursor, sLast[cursor], dicPosFirst, dicPosLast)

    return ''.join(reversed(temp))


inputfile = '221122/221122_Q2_input2.txt'
sInput = PARSE(inputfile)
sOutput = INVERSION(sInput)
WRITE_OUTPUT(sOutput)