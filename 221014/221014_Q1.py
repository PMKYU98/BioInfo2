sInput= '''
PLEASANTLY
MEANLY
'''

edit = 1

def PRINT_MATRIX(matScore):
    for l in matScore:
        print('\t'.join([str(i) for i in l]))

def CALCULATE(sV, sW, x, y, matScore):
    if x == 0:
        return matScore[y-1][x] + edit
    if y == 0:
        return matScore[y][x-1] + edit

    scoreDown = matScore[y-1][x] + edit
    scoreRight = matScore[y][x-1] + edit
    if sV[y-1] == sW[x-1]:
        scoreDiagonal = matScore[y-1][x-1]
    else:
        scoreDiagonal = matScore[y-1][x-1] + 1

    return min(scoreDown, scoreRight, scoreDiagonal)

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

matScore = INITIALIZE(sV, sW, n, m)
matScore = TOUR(sV, sW, n, m, matScore)
#PRINT_MATRIX(matScore)

print(matScore[n][m])