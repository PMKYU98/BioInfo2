sInput= '''
PAWHEAE
HEAGAWGHEE
'''

match = 1
penalty = -2

def PRINT_MATRIX(matScore):
    for l in matScore:
        print('\t'.join([str(i) for i in l]))

def CALCULATE(sV, sW, x, y, matScore):
    scoreDown = matScore[y-1][x] + penalty
    scoreRight = matScore[y][x-1] + penalty
    if sV[y-1] == sW[x-1]:
        scoreDiagonal = matScore[y-1][x-1] + match
    else:
        scoreDiagonal = matScore[y-1][x-1] + penalty

    return max(scoreDown, scoreRight, scoreDiagonal, 0)

def INITIALIZE(sV, sW, n, m):
    matScore = [[0] * (m+1) for i in range(n+1)]

    return matScore

def TOUR(sV, sW, n, m, matScore):
    for y in range(1, n+1):
        for x in range(1, m+1):
            matScore[y][x] = CALCULATE(sV, sW, x, y, matScore)

    return matScore

sW, sV = sInput.split('\n')[1:-1]
n, m = len(sV), len(sW)

matScore = INITIALIZE(sV, sW, n, m)
matScore = TOUR(sV, sW, n, m, matScore)
PRINT_MATRIX(matScore)