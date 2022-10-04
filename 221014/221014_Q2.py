sInput= '''
GTAGGCTTAAGGTTA
TAGATA
'''

match = 1
penalty = -1

def PRINT_MATRIX(matScore):
    for l in matScore:
        print('\t'.join([str(i) for i in l]))

def CALCULATE(sV, sW, x, y, matScore):
    if x == 0:
        return matScore[y-1][x] + penalty

    scoreDown = matScore[y-1][x] + penalty
    scoreRight = matScore[y][x-1] + penalty
    if sV[y-1] == sW[x-1]:
        scoreDiagonal = matScore[y-1][x-1] + match
    else:
        scoreDiagonal = matScore[y-1][x-1] + penalty

    return max(scoreDown, scoreRight, scoreDiagonal)

def INITIALIZE(sV, sW, n, m):
    matScore = [[0] * (m+1) for i in range(n+1)]

    for y in range(1,n+1):
        matScore[y][0] = CALCULATE(sV, sW, 0, y, matScore)

    return matScore

def TOUR(sV, sW, n, m, matScore):
    for y in range(1, n+1):
        for x in range(1, m+1):
            matScore[y][x] = CALCULATE(sV, sW, x, y, matScore)

    return matScore

def BACKTRACK(n, m, sV, sW, matScore):
    i, j = n, m
    subseq1 = []
    subseq2 = []
    while(i >= 1 and j >= 1):
        if matScore[i][j] == matScore[i][j-1] - 1:
            subseq1.append('-')
            subseq2.append(sW[j-1])
            j -= 1
        elif matScore[i][j] == matScore[i-1][j] - 1: 
            subseq1.append(sV[i-1])
            subseq2.append('-')
            i -= 1
        else:
            subseq1.append(sV[i-1])
            subseq2.append(sW[j-1])
            i -= 1
            j -= 1

    substr1 = ''.join(reversed(subseq1))
    substr2 = ''.join(reversed(subseq2))

    print(matScore[n][m])
    print(substr2)
    print(substr1)

sW, sV = sInput.split('\n')[1:-1]
n, m = len(sV), len(sW)

matScore = INITIALIZE(sV, sW, n, m)
matScore = TOUR(sV, sW, n, m, matScore)
#PRINT_MATRIX(matScore)

maxScore = max(matScore[n])
maxX = matScore[n].index(maxScore)

BACKTRACK(n, maxX, sV, sW, matScore)