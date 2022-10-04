sBLOSUM62 = '''
   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7
'''

aminoacids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
            'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

BLOSUM62 = {}
for l in sBLOSUM62.strip().split('\n')[1:]:
    temp = l.split(' ')
    aa = temp[0]
    scores = [int(i) for i in temp[1:] if i != '']
    BLOSUM62[aa] = dict(zip(aminoacids, scores))

gapopening = -11
gap = -1
none = 'none'
left = 'left'
up = 'up'
diag = 'diag'

def PRINT_MATRIX(mat):
    for l in mat:
        print('\t'.join([str(i) for i in l]))

def CALCULATE(x, y, matScore, matArrow):
    if x == 0:
        return (matScore[y-1][x] + gap), up
    if y == 0:
        return matScore[y][x-1] + gap, left

    if matArrow[y-1][x] != diag:
        scoreDown = matScore[y-1][x] + gap
    else:
        scoreDown = matScore[y-1][x] + gapopening

    if matArrow[y][x-1] != diag:
        scoreRight = matScore[y][x-1] + gap
    else:
        scoreRight = matScore[y][x-1] + gapopening

    scoreDiagonal = matScore[y-1][x-1] + BLOSUM62[sV[y-1]][sW[x-1]]
    
    if scoreDown >= scoreRight:
        if scoreDown >= scoreDiagonal:
            return scoreDown, up
        else:
            return scoreDiagonal, diag
    elif scoreRight >= scoreDiagonal:
        return scoreRight, left
    else:
        return scoreDiagonal, diag

def INITIALIZE(n, m):
    matScore = [[0] * (m+1) for i in range(n+1)]
    matArrow = [[none] * (m+1) for i in range(n+1)]

    for x in range(1,m+1):
        matScore[0][x], matArrow[0][x] = CALCULATE(x, 0, matScore, matArrow)

    for y in range(1,n+1):
        matScore[y][0], matArrow[y][0] = CALCULATE(0, y, matScore, matArrow)

    return matScore, matArrow


def TOUR(n, m, sV, sW, matScore, matArrow):
    for y in range(1, n+1):
        for x in range(1, m+1):
            matScore[y][x], matArrow[y][x] = CALCULATE(x, y, matScore, matArrow)

    return matScore, matArrow

def BACKTRACK(n, m, sV, sW, matScore, matArrow):
    i, j = n, m
    subseq1 = []
    subseq2 = []
    while(i >= 1 or j >= 1):
        if matArrow[i][j] == left:
            subseq1.append('-')
            subseq2.append(sW[j-1])
            j -= 1
        elif matArrow[i][j] == up: 
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
    print(substr1)
    print(substr2)


sInput= '''
PRTEINS
PRTWPSEIN
'''

sV, sW = sInput.split('\n')[1:-1]
n, m = len(sV), len(sW)

matScore, matArrow = INITIALIZE(n, m)
# matArrow
# 0: None, 1: Up, 2: Left, 3: Diagonal
matScore, matArrow = TOUR(n, m, sV, sW, matScore, matArrow)
PRINT_MATRIX(matScore)
PRINT_MATRIX(matArrow)
BACKTRACK(n, m, sV, sW, matScore, matArrow)