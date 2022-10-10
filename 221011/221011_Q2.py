sInput1 = '''
4
1
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''

sInput = sInput1

def PRINT_MATRIX(mat):
    for l in mat:
        print('\t'.join([str(i) for i in l]))

def MATRIX_TO_FILE(mat):
    temp = ['']
    for l in mat:
        temp.append('\t'.join([str(i) for i in l]))
    temp.append('')

    sOutput = '\n'.join(temp)
    with open('221011/221011_Q1_output.txt', 'w') as f:
        f.write(sOutput)

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])
    j = int(lines[1])

    matDist = []
    for l in lines[2:]:
        matDist.append([int(x) for x in l.split(' ') if x != ''])

    return n, j, matDist

def LIMBLENGTH(i):
    global n, matDist
    lstDist = matDist[i]

    temp = []
    for j in range(n):
        if j == i: continue
        for k in range(j, n):
            if k == i: continue
            dist = lstDist[j] + lstDist[k] - matDist[j][k]
            temp.append(int(dist/2))
    
    print(min(temp))

n, j, matDist = PARSE(sInput)
LIMBLENGTH(j)