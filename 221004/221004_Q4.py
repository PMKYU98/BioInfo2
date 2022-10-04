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

gap = -1
gapopening = -11 + gap
none = 'none'
left = 'left'
up = 'up'
diag = 'diag'

def PRINT_MATRIX(mat):
    for l in mat:
        print('\t'.join([str(i) for i in l]))
    print('')

def CALCULATE(x, y):
    matXGap[y][x] = max(gapopening + matScore[y][x-1], gap + matXGap[y][x-1], gapopening + matYGap[y][x-1])
    matYGap[y][x] = max(gapopening + matScore[y-1][x], gapopening + matXGap[y-1][x], gap + matYGap[y-1][x])

    matchScore = BLOSUM62[sV[y-1]][sW[x-1]]
    matScore[y][x] = matScore[y-1][x-1] + matchScore

    what_is_max = max(matScore[y][x], matXGap[y][x], matYGap[y][x])

    if what_is_max == matXGap[y][x]: matArrow[y][x] = left
    elif what_is_max == matYGap[y][x]: matArrow[y][x] = up
    elif what_is_max == matScore[y][x]: matArrow[y][x] = diag

    matScore[y][x] = what_is_max

def INITIALIZE(n, m):
    matScore = [[0] * (m+1) for i in range(n+1)]
    matMatch = [[0] * (m+1) for i in range(n+1)]
    matXGap = [[0] * (m+1) for i in range(n+1)]
    matYGap = [[0] * (m+1) for i in range(n+1)]
    matArrow = [[none] * (m+1) for i in range(n+1)]

    for x in range(1,m+1):
        matMatch[0][x] = NEG_INF
        matXGap[0][x] = gapopening + gap * (x-1)
        matYGap[0][x] = NEG_INF
        matScore[0][x] = max(matMatch[0][x], matXGap[0][x], matYGap[0][x])
        matArrow[0][x] = left

    for y in range(1,n+1):
        matMatch[y][0] = NEG_INF
        matXGap[y][0] = NEG_INF
        matYGap[y][0] = gapopening + gap * (y-1)
        matScore[y][0] = max(matMatch[y][0], matXGap[y][0], matYGap[y][0])
        matArrow[y][0] = up

    return matScore, matMatch, matXGap, matYGap, matArrow


def TOUR():
    for y in range(1, n+1):
        for x in range(1, m+1):
            CALCULATE(x, y)


def BACKTRACK(n, m):
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


sInput3_2 = '''
LIEWLRWM
EIQGK
'''

sInput4 = '''
PRTEINS
PRTWPSEIN
'''

sInput5 = '''
LVYCAMQMAPAHRFRQARHHWASIPWEYEMRLWWTSVFNFRKNAWITYRYWTWHHSTIWWEWTKNPIAETGDYYCGSEDTPSDM
RHHWASGPWTYEMYMEKHLWWTSFFNFRKWCPDQQTITERYHHSTIWVERAMWTKNPIQETGDYYCGSEDTPHDM
'''

sInput6_1 = '''
PHPP
PHYASNWLWP
'''

sInput = sInput6_1

sV, sW = sInput.split('\n')[1:-1]
n, m = len(sV), len(sW)

NEG_INF = max(n, m) * gapopening - 1

matScore, matMatch, matXGap, matYGap, matArrow = INITIALIZE(n, m)
TOUR()
PRINT_MATRIX(matScore)
PRINT_MATRIX(matXGap)
PRINT_MATRIX(matYGap)
PRINT_MATRIX(matArrow)
BACKTRACK(n, m)