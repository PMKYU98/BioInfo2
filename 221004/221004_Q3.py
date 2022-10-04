sInput= '''
CGTTCTAGAAGCAGAGGGCTGCAGGTTCTTGCTCTGCCATTCTTTTAAGATCATGCAGACATAACCAAGCCTCTAGGCGGATATTTACTAGTGCATCTGGGGCCCCCCCAAGCCGCGAGCAGAATACTACTGTGGTCTCAGGTAAAAGCGCCAGTCCTAGGGACAATTACTTTGTTTATAATTGGGTTCGTCTATCCTTAACATGAGGTGATATTTCTTGTGCGCAGATTCTGCACACCCAACGGTACGTCTCCAGTAGGCCACGAACCGCTCTGGGCGCCCCTGACTGCCCCTATAAGAATGACGCTCTTGACGGTAGCCTTGACAATTCGCATTGGTTCAGTCCGCCCTCGTCTAACGAGACCCCGTACGCCGGGAGCATATGCAGAGGAATGTCTGGCCAATATAGAATCATAGGCCGCCTGGTGGCATCATTATAAATCACCGGTGCCGGGTCTTAGCGACTTGAGGAGGGGGTATATTGACTCGTCACAGGGCTATCTGCTCCTGGTGATAATGTATACTTAAAGCAATTGAACACAATTAATCAATGGCTTAGTAGTAATTGAATAAGTAAATTACCTGGGCTCAATCGGCTCTCTGCAAACGATGTGGTAACTCCGCGTACGTGGCCGAACACCGGCCGAAAAGTCACTCACTTCCCCTCACGTTAGTAGGTACCGGTATCGAGATTATCGCACAGAGATGAGTCTGTACGAGAGATACTCCTGACCATCATTCTATAAGAGCACCAGGCATGAGCGGGCTCGCCCTATGATACCGCCTACGGACGGACCCGACAAATTTCTGGTACCCGAGCTAGCTTATTGAAACATCCGACTCAGAACCAGCAAGTATAGATTTTGTTTCACAACTGACCCCCAACCTAGTTAATGGTA
TCTTAGGTTCCGGTATTGTTGATTCGTCGCACAGAGGTGAGTCTTATAGAGATACTCTTCAACCATCATTCTTAAGGGCTCACCAGGCGGTTAGCAAGCTCGCCTATAATTACTGCCTCCGATGACCCGGGAAGCCTGGGACCGAGCCGTGGGTGTACTGTAAAAACACCCGACTCAGGACCAAATGTATAAGATTCAGGTCTTACAGATTAATCCCGAACCACCAAACGGTAATACCCATTAAGTTCTTATCTCTACCAGGACTGAGTTCCTGTGAGCAAGAGGTAATTCACTGTTCATGCGAGGAAGAATCCTCTCGGAACCTCTCGCACTACCAAGCGCGGCGCTGCCTCTTACGTCTGCAGGTCCTGATACTAACTTAGATGCGTGAGAATCCGATTCACAGAGAAGCTGTACCGTCGCAGGCCGAGGATCGTCATAATCCTATACCACCGAGTTTTCACAGACACTCAATAGCGTCTCTAGTCGGACGACCGTTAGACGATCATCGCACTAGAACCGGTTAGTATTCGCTGCGGCACGCTATCCGCTGCTGATGACCAAACCTCGCTCCATTGCTCAAGGACACCGAACAAAGTGCAGGTCTAGTAATCGGGCGTTCAACACGAGTCTAGTTGGGGAGCCCCTAATTTTTTATACCCTCTCACCCGATTTTATCGTTAATCATTCGGTGTCGACTTTGAGCCCCACTCGTCCCAATTTAGGCAGACGCACCCCGTTTTGCTTTGCATTGACTTAGTGATAATATAGTTCCTTACGTTGTATAAAATAGCCATTGCGAAACAGGCAAATCCGCCGAGTTGTATCGTGACCTAACGATAATTAAAACAACCTGTGTTGCAGGCTCGCAGCGTTATAAAGGCAATGTTTGTATCCTTTGCGCATCTGACGACTTCTCACAACTTGGGCTCGTGATAAGAATAG
'''

match = 1
penalty = -2

def PRINT_MATRIX(matScore):
    for l in matScore:
        print('\t'.join([str(i) for i in l]))

def CALCULATE(sV, sW, x, y, matScore):
    if x == 0:
        return matScore[y-1][x] + penalty
    if y == 0:
        return matScore[y][x-1] + penalty

    if x == len(sW):
        scoreDown = matScore[y-1][x] + penalty * 10
    else:
        scoreDown = matScore[y-1][x] + penalty

    if y == len(sV):
        scoreRight = matScore[y][x-1] + penalty * 10
    else:
        scoreRight = matScore[y][x-1] + penalty

    if sV[y-1] == sW[x-1]:
        scoreDiagonal = matScore[y-1][x-1] + match
    else:
        scoreDiagonal = matScore[y-1][x-1] + penalty

    return max(scoreDown, scoreRight, scoreDiagonal)

def INITIALIZE(sV, sW, n, m):
    matScore = [[0] * (m+1) for i in range(n+1)]

    for x in range(1,m+1):
        matScore[0][x] = CALCULATE(sV, sW, x, 0, matScore)

    for y in range(1,n+1):
        matScore[y][0] = CALCULATE(sV, sW, 0, y, matScore)

    return matScore

def TOUR(sV, sW, n, m, matScore):
    for y in range(1, n+1):
        for x in range(1, m+1):
            matScore[y][x] = CALCULATE(sV, sW, x, y, matScore)

    return matScore

sV, sW = sInput.split('\n')[1:-1]
n, m = len(sV), len(sW)

suffix_sV = []
for i in range(len(sV)):
    suffix_sV.append(sV[n-i-1:])

prefix_sW = []
for i in range(len(sW)):
    prefix_sW.append(sW[:i+1])

scores = {}
for suffix in suffix_sV:
    for prefix in prefix_sW:
        _n = len(suffix)
        _m = len(prefix)
        matScore = INITIALIZE(suffix, prefix, _n, _m)
        matScore = TOUR(suffix, prefix, _n, _m, matScore)

        if suffix == 'HEAE' and prefix == 'HEA':
            PRINT_MATRIX(matScore)

        scores[(suffix, prefix)] = matScore[_n][_m]

maxScore = max(scores.values())
print(maxScore)
maxScoreKeys = [k for k in scores.keys() if scores[k] == maxScore]
print('\n'.join(maxScoreKeys[0]))