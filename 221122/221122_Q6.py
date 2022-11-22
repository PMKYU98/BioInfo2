def PARSE(fInput):
    with open(fInput, 'r') as f:
        lines = f.readlines()

    sInput = lines[0].strip() + '$'
    lstPattern = []
    for line in lines[1:]:
        lstPattern.append(line.strip())

    return sInput, lstPattern

def WRITE_OUTPUT(sOutput):
    outputfile = '221122/221122_Q6_output.txt'
    sOutput = [str(x) for x in sorted(sOutput)]
    with open(outputfile, 'w') as f:
        f.write(' '.join(sOutput))

    return

def FIRST_OCCURRENCE(sLast):
    alphabets = ['A', 'C', 'G', 'T', '$']
    sFirst = sorted(sLast)
    return {symbol: sFirst.index(symbol) for symbol in alphabets}

def CYCLIC_ROTATION(lstInput):
    matInput = []
    for i in range(len(lstInput)):
        suff_pref = lstInput[i:]
        suff_pref.extend(lstInput[:i])
        matInput.append(suff_pref)

    return sorted(matInput)

def BWT(matInput):
    return ''.join([row[-1] for row in matInput])

def PARTIAL_SUFFIX_ARRAY(sInput, K):
    lSuffices = sorted([sInput[i:] for i in range(len(sInput))])
    lSufficesIndex = [sInput.index(suffix) for suffix in lSuffices]
    lPartialSuffix = [(i, lSufficesIndex[i]) for i in range(len(lSufficesIndex)) if lSufficesIndex[i] % K == 0]
    return lPartialSuffix

def SUFFIX_ARRAY(sInput):
    lSuffices = sorted([sInput[i:] for i in range(len(sInput))])
    lSufficesIndex = [sInput.index(suffix) for suffix in lSuffices]
    return lSufficesIndex

def CHECKPOINT_ARRAY(sLast, K):
    lstCheckpoint = [[0, 0, 0, 0, 0]] # A, C, G, T, $
    alphabet = {'A': 0, 'C': 1, 'G': 2, 'T': 3, '$': 4}
    for i in range(len(sLast)):
        temp = lstCheckpoint[-1].copy()
        x = sLast[i]
        temp[alphabet[x]] += 1
        lstCheckpoint.append(temp)

    return [lstCheckpoint[i] for i in range(len(lstCheckpoint)) if i % K == 0]

def COUNT(symbol, i, sLast, lstCheckpoint, K):
    alphabet = {'A': 0, 'C': 1, 'G': 2, 'T': 3, '$': 4}
    div = i // K
    checkpoint = lstCheckpoint[div][alphabet[symbol]]

    rest = sLast[div * K : i]
    
    return checkpoint + rest.count(symbol)
    
def BWMATCHING(sLast, pattern, K):
    top, bottom = 0, len(sLast) - 1
    dicFirstOccur = FIRST_OCCURRENCE(sLast)
    lstCheckpoint = CHECKPOINT_ARRAY(sLast, K)

    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            if symbol in sLast[top:bottom+1]:
                count_top = COUNT(symbol, top, sLast, lstCheckpoint, K)
                count_bottom = COUNT(symbol, bottom + 1, sLast, lstCheckpoint, K)

                top = dicFirstOccur[symbol] + count_top
                bottom = dicFirstOccur[symbol] + count_bottom - 1
            else:
                return 0
        else:
            return top, bottom
    
    return -1


inputfile = '221122/221122_Q6_input2.txt'
K = 7
sString, lstPattern = PARSE(inputfile)
sLast = BWT(CYCLIC_ROTATION(list(sString)))
lPartialSuffix = PARTIAL_SUFFIX_ARRAY(sString, K)
lSuffix = SUFFIX_ARRAY(sString)

answer = []
for pattern in lstPattern:
    temp = BWMATCHING(sLast, pattern, K)

    if temp != 0 and temp != -1:
        top, bottom = temp
        answer.extend(lSuffix[top:bottom+1])

WRITE_OUTPUT(answer)