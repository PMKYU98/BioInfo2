def PARSE(fInput):
    with open(fInput, 'r') as f:
        lines = f.readlines()
        sInput = lines[0].strip()

        lPatterns = [line.strip() for line in lines[1:]]

    return sInput, lPatterns

def SUFFIX_ARRAY(sInput):
    lSuffices = sorted([sInput[i:] for i in range(len(sInput))])
    lSufficesIndex = [str(sInput.index(suffix)) for suffix in lSuffices]
    return lSufficesIndex

def PATTERN_MATCHING(lPatterns, sString, lSufficesIndex):
    

inputfile = '221115/221115_Q5_input1.txt'
sInput, lPatterns = PARSE(inputfile)
lSufficesIndex = SUFFIX_ARRAY(sInput)
print(', '.join(lSufficesIndex))