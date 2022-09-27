sPAM250 = '''
   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
'''

aminoacids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
            'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

PAM250 = {}
for l in sPAM250.strip().split('\n')[1:]:
    temp = l.split(' ')
    aa = temp[0]
    scores = [int(i) for i in temp[1:] if i != '']
    PAM250[aa] = dict(zip(aminoacids, scores))

gap = -5

def PRINT_MATRIX(matScore):
    for l in matScore:
        print('\t'.join([str(i) for i in l]))

def CALCULATE(x, y, matScore):
    if x == 0:
        return 0
    if y == 0:
        return 0

    scoreDown = matScore[y-1][x] + gap
    scoreRight = matScore[y][x-1] + gap
    scoreDiagonal = matScore[y-1][x-1] + PAM250[sV[y-1]][sW[x-1]]
    return max(0, scoreDown, scoreRight, scoreDiagonal)

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

def FIND_MAX(matScore):
    maxX, maxY, maxScore = 0, 0, 0
    for y in range(len(matScore)):
        for x in range(len(matScore[y])):
            if matScore[y][x] > maxScore:
                maxScore = matScore[y][x]
                maxX, maxY = x, y

    return maxX, maxY, maxScore


def BACKTRACK(matScore):
    i, j = n, m
    subseq1 = []
    subseq2 = []
    while(i >= 1 and j >= 1):
        if matScore[i][j] == matScore[i][j-1] - 5:
            subseq1.append('-')
            subseq2.append(sW[j-1])
            j -= 1
        elif matScore[i][j] == matScore[i-1][j] - 5: 
            subseq1.append(sV[i-1])
            subseq2.append('-')
            i -= 1
        else:
            subseq1.append(sV[i-1])
            subseq2.append(sW[j-1])
            if matScore[i-1][j-1] == 0:
                break

            i -= 1
            j -= 1
            

    substr1 = ''.join(reversed(subseq1))
    substr2 = ''.join(reversed(subseq2))

    print(matScore[n][m])
    print(substr1)
    print(substr2)


sInput= '''
MEANLY
PENALTY
'''

sV, sW = sInput.split('\n')[1:-1]
n, m = len(sV), len(sW)

matScore = INITIALIZE(n, m)
matScore = TOUR(n, m, sV, sW, matScore)
PRINT_MATRIX(matScore)
maxX, maxY, maxScore = FIND_MAX(matScore)
print(maxX, maxY, maxScore)
BACKTRACK(matScore)