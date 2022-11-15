def PARSE(fInput):
    with open(fInput, 'r') as f:
        lines = f.readlines()
        sInput = lines[0].strip() +'$'

        lPatterns = [line.strip() for line in lines[1:]]

    return sInput, lPatterns

def SUFFIX_ARRAY(sInput):
    lSuffices = sorted([sInput[i:] for i in range(len(sInput))])
    lSufficesIndex = [str(sInput.index(suffix)) for suffix in lSuffices]
    return lSufficesIndex

def PATTERN_MATCHING(lPatterns, sString, lSufficesIndex):
    matched = []
    for pattern in lPatterns:
        length = len(pattern)
        for idx in lSufficesIndex:
            i = int(idx)
            if i >= len(sString) - length: continue
            if sString[i:][:length] > pattern: break
            if pattern == sString[i:][:length]: matched.append(i)
    return [str(x) for x in sorted(matched)]

inputfile = '221115/221115_Q5_input2.txt'
sInput, lPatterns = PARSE(inputfile)
lSufficesIndex = SUFFIX_ARRAY(sInput)
matched = PATTERN_MATCHING(lPatterns, sInput, lSufficesIndex)

print(' '.join(matched))