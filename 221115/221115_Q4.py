def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()

    return sInput

def SUFFIX_ARRAY(sInput):
    lSuffices = sorted([sInput[i:] for i in range(len(sInput))])
    lSufficesIndex = [str(sInput.index(suffix)) for suffix in lSuffices]
    print(', '.join(lSufficesIndex))

inputfile = '221115/221115_Q4_input2.txt'
sInput = PARSE(inputfile)
SUFFIX_ARRAY(sInput)