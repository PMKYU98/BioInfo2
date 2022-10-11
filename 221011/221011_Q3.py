sInput1 = '''
4
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''

sInput = sInput1

def PRINT_MATRIX(mat):
    for l in mat:
        print('\t'.join([str(i) for i in l]))

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])

    matDist = []
    for l in lines[1:]:
        matDist.append([int(x) for x in l.split(' ') if x != ''])

    return n, matDist

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
    
    return min(temp)

def MAKE_BALD(n, j, matDist):
    limblength = LIMBLENGTH(j)
    for i in range(n+1):
        print(i, j)
        if i != j:
            matDist[i][j] -= limblength
            matDist[j][i] = matDist[i][j]

# find i,n,k which is Di,k = Di,n + Dn,k
def FIND_INK(n, j, matDist):
    trio = None
    for i in range(n+1):
        if j == i: continue
        if trio is not None: break
        for k in range(n+1):
            if k == i or j == k or j == i: continue
            if matDist[i][k] == matDist[i][j] + matDist[j][k]:
                trio = (i, j, k)
                break

    return trio

def TRIM(n, matDist):
    temp = []
    for i in range(len(matDist)):
        if i != n:
            temp_row = []
            for j in range(len(matDist[i])):
                if j != n:
                    temp_row.append(matDist[i][j])
            temp.append(temp_row)

    return temp

def ADDITIVE_PHYLOGENY(n, j, matDist):
    print('ADDITIVE_PHYLOGENY %d, %d----------' % (n, j))
    if n == 1:
        PRINT_MATRIX(matDist)
        return
    
    print('\nD')
    PRINT_MATRIX(matDist)
    limblength = LIMBLENGTH(j)
    print('Limblength: ', LIMBLENGTH(j))
    MAKE_BALD(n, j, matDist)
    print('\nDbald')
    PRINT_MATRIX(matDist)

    ink = FIND_INK(n, j, matDist)
    if ink is None:
        print('No degenerate')
        ADDITIVE_PHYLOGENY(n, j-1, matDist)
    else: 
        i, j, k = ink
        print('i, n, k = ', i, j, k)
        x = matDist[i][j]
        print('x = ', x)

        matDist = TRIM(n, matDist)

        ADDITIVE_PHYLOGENY(n-1, n-1, matDist)
    

    

n, matDist = PARSE(sInput)
_n = n-1
_matDist = matDist
ADDITIVE_PHYLOGENY(_n, _n, _matDist)