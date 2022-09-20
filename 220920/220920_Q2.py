sInput = '''
4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2
'''     

def PARSE_INPUT(sInput):
    lines = sInput.split('\n')[1:-1]
    n, m = [int(i) for i in lines[0].split(' ')]

    lDown = []
    idx = 1
    for l in lines[1:]:

        if l.startswith('-'): break
        lDown.append([int(x) for x in l.split(' ')])
        idx += 1
        
    lRight = []
    for l in lines[idx+1:]:
        lRight.append([int(x) for x in l.split(' ')])

    return n, m, lDown, lRight

def PRINT_MATRIX(matScore):
    for l in matScore:
        print('\t'.join([str(i) for i in l]))

def CALCULATE(x, y, lDown, lRight, matScore):
    if x == 0:
        return matScore[y-1][x] + lDown[y-1][x]
    if y == 0:
        return matScore[y][x-1] + lRight[y][x-1]

    scoreDown = matScore[y-1][x] + lDown[y-1][x]
    scoreRight = matScore[y][x-1] + lRight[y][x-1]
    return max(scoreDown, scoreRight)

def INITIALIZE(n, m, lDown, lRight):
    matScore = [[0] * (n+1) for i in range(m+1)]

    for x in range(1,n+1):
        matScore[0][x] = CALCULATE(x, 0, lDown, lRight, matScore)

    for y in range(1,m+1):
        matScore[y][0] = CALCULATE(0, y, lDown, lRight, matScore)

    return matScore

def TOUR(n, m, lDown, lRight, matScore):
    for y in range(1, m+1):
        for x in range(1, n+1):
            matScore[y][x] = CALCULATE(x, y, lDown, lRight, matScore)

    return matScore

n, m, lDown, lRight = PARSE_INPUT(sInput)
matScore = INITIALIZE(n,m,lDown,lRight)
PRINT_MATRIX(matScore)
print('')
matScore = TOUR(n,m,lDown,lRight,matScore)
PRINT_MATRIX(matScore)