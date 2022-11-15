def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()

    return sInput

def WRITE_OUTPUT(sOutput):
    outputfile = '221115/221115_Q4_output.txt'
    with open(outputfile, 'w') as f:
        f.write(sOutput)

def SUFFIX_ARRAY(sInput):
    lSuffices = sorted([sInput[i:] for i in range(len(sInput))])
    lSufficesIndex = [str(sInput.index(suffix)) for suffix in lSuffices]
    return ', '.join(lSufficesIndex)

inputfile = '221115/221115_Q4_input3.txt'
sInput = PARSE(inputfile)
sOutput = SUFFIX_ARRAY(sInput)
WRITE_OUTPUT(sOutput)