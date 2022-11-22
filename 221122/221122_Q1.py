def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()

    return list(sInput)

def WRITE_OUTPUT(sBWT):
    outputfile = '221122/221122_Q1_output.txt'
    with open(outputfile, 'w') as f:
        f.write(sBWT)

    return

def CYCLIC_ROTATION(lstInput):
    matInput = []
    for i in range(len(lstInput)):
        suff_pref = lstInput[i:]
        suff_pref.extend(lstInput[:i])
        matInput.append(suff_pref)

    return sorted(matInput)

def BWT(matInput):
    return ''.join([row[-1] for row in matInput])

inputfile = '221122/221122_Q1_input1.txt'
lstInput = PARSE(inputfile)
matInput = CYCLIC_ROTATION(lstInput)
WRITE_OUTPUT(BWT(matInput))