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

gap = -5

def PRINT_MATRIX(matScore):
    for l in matScore:
        print('\t'.join([str(i) for i in l]))

def CALCULATE(x, y, matScore):
    if x == 0:
        return matScore[y-1][x] + gap
    if y == 0:
        return matScore[y][x-1] + gap

    scoreDown = matScore[y-1][x] + gap
    scoreRight = matScore[y][x-1] + gap
    scoreDiagonal = matScore[y-1][x-1] + BLOSUM62[sV[y-1]][sW[x-1]]
    return max(scoreDown, scoreRight, scoreDiagonal)

def INITIALIZE(n, m):
    matScore = [[0] * (m+1) for i in range(n+1)]

    for x in range(1,m+1):
        matScore[0][x] = CALCULATE(x, 0, matScore)

    for y in range(1,n+1):
        matScore[y][0] = CALCULATE(0, y, matScore)

    return matScore


def TOUR(n, m, sV, sW, matScore):
    for y in range(1, n+1):
        for x in range(1, m+1):
            matScore[y][x] = CALCULATE(x, y, matScore)

    return matScore

def BACKTRACK(n, m, sV, sW, matScore):
    i, j = n, m
    subseq1 = []
    subseq2 = []
    while(i >= 1 or j >= 1):
        if matScore[i][j] == matScore[i][j-1] + gap:
            subseq1.append('-')
            subseq2.append(sW[j-1])
            j -= 1
        elif matScore[i][j] == matScore[i-1][j] + gap: 
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

def MIDDLEEDGE(n, m, sV, sW, matScore):
    i, j = n, m
    middleCol = m / 2
    subseq1 = []
    subseq2 = []
    arrow = 'none'
    while(i >= 1 or j >= 1):
        if matScore[i][j] == matScore[i][j-1] + gap:
            j -= 1
            arrow = 'left'
        elif matScore[i][j] == matScore[i-1][j] + gap: 
            i -= 1
            arrow = 'up'
        else:
            i -= 1
            j -= 1
            arrow = 'diag'

        if j <= middleCol:
            break
    
    if arrow == 'left':
        return '(%d, %d) (%d, %d)' % (i, j, i+1, j)
    elif arrow == 'up':
        return '(%d, %d) (%d, %d)' % (i, j, i, j+1)
    else:
        return '(%d, %d) (%d, %d)' % (i, j, i+1, j+1)


sInput= '''
GAGA
GAT
'''

sV, sW = sInput.split('\n')[1:-1]
n, m = len(sV), len(sW)

matScore = INITIALIZE(n, m)
matScore = TOUR(n, m, sV, sW, matScore)
PRINT_MATRIX(matScore)

print(MIDDLEEDGE(n, m, sV, sW, matScore))