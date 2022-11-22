def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()
        lstPattern = f.readline().strip().split(' ')

    return sInput, lstPattern

def WRITE_OUTPUT(sOutput):
    outputfile = '221122/221122_Q5_output.txt'
    with open(outputfile, 'w') as f:
        f.write(sOutput)

    return

def FIRST_OCCURRENCE(symbol, sFirst):
    return sFirst.index(symbol)

def COUNT(symbol, n, sLast):
    return sLast[:n].count(symbol)

def BWMATCHING(sFirst, sLast, pattern):
    top, bottom = 0, len(sLast) - 1

    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            if symbol in sLast[top:bottom+1]:
                top = FIRST_OCCURRENCE(symbol, sFirst) + COUNT(symbol, top, sLast)
                bottom = FIRST_OCCURRENCE(symbol, sFirst) + COUNT(symbol, bottom + 1, sLast) - 1
            else:
                return 0
        else:
            return bottom - top + 1

inputfile = '221122/221122_Q5_input1.txt'
sLast, lstPattern = PARSE(inputfile)
sFirst = ''.join(sorted(sLast))

answer = [str(BWMATCHING(sFirst, sLast, pattern)) for pattern in lstPattern]
WRITE_OUTPUT(' '.join(answer))