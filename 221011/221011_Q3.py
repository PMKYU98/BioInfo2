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

def MAKE_BALD(n, matDist):
    limblength = LIMBLENGTH(n)
    for j in range(n):
        matDist[n][j] -= limblength
        matDist[j][n] = matDist[n][j]

# find i,n,k which is Di,k = Di,n + Dn,k
def FIND_INK(n, matDist):
    trio = None
    for i in range(n):
        if n == i: continue
        if trio is not None: break
        for k in range(i, n):
            if n == k or n == i: continue
            if matDist[i][k] == matDist[i][n] + matDist[n][k]:
                trio = (i, n, k)
                break

    return trio

def TRIM(n, matDist):
    return [matDist[i][:n] for i in range(n)]

def ADDITIVE_PHYLOGENY(n, matDist):
    global lstTree, maxnode

    if n == 1:
        lstTree.append((0, 1, matDist[0][1]))
        lstTree.append((1, 0 , matDist[1][0]))
    
    print('')
    PRINT_MATRIX(matDist)
    limblength = LIMBLENGTH(n)
    print(LIMBLENGTH(n))
    MAKE_BALD(n, matDist)
    print('')
    PRINT_MATRIX(matDist)

    i, _, k = FIND_INK(n, matDist)
    x = matDist[i][n]

    lstTree.append((n, maxnode, limblength))
    lstTree.append((maxnode, n, limblength))
    maxnode += 1
    print(lstTree)

    matDist = TRIM(n, matDist)
    ADDITIVE_PHYLOGENY(n-1, matDist)
    

    

n, matDist = PARSE(sInput)
PRINT_MATRIX(matDist)
_n = n-1
_matDist = matDist
maxnode = n
lstTree = []
ADDITIVE_PHYLOGENY(_n, _matDist)
print(lstTree)