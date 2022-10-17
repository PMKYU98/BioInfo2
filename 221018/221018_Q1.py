sInput1 = '''
4
0   23  27  20
23  0   30  28
27  30  0   30
20  28  30  0
'''

sInput2 = '''
4
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''

sInput = sInput2

def PRINT_MATRIX(mat):
    for l in mat:
        print('\t'.join([str(i) for i in l]))

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])

    matD = []
    for l in lines[1:]:
        matD.append([int(x) for x in l.split(' ') if x != ''])

    return n, matD

def NEIGHBOR_MATRIX(n, matD):
    lstTotalDist = [sum(row) for row in matD]

    matDstar = []
    for i in range(len(matD)):
        newRow = []
        for j in range(len(matD[i])):
            if i == j: newRow.append(0)
            else: newRow.append((n - 2) * matD[i][j] - lstTotalDist[i] - lstTotalDist[j])
        matDstar.append(newRow)

    return matDstar

    
n, matD = PARSE(sInput)
matDstar = NEIGHBOR_MATRIX(n, matD)
PRINT_MATRIX(matDstar)
