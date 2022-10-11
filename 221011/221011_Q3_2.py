sInput1 = '''
4
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''

sInput2 = '''
3
0   13  15
13  0   12
15  12  0
'''

sInput = sInput1

def PRINT_MATRIX(mat, newline=False):
    if newline: print('')
    for l in mat:
        print('\t'.join([str(i) for i in l]))

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])

    matDist = []
    for l in lines[1:]:
        matDist.append([int(x) for x in l.split(' ') if x != ''])

    return n, matDist

def PRINT_TREE(tree):
    print('------------')
    for edge in tree:
        print('%d->%d:%d' % (edge[0], edge[1], edge[2]))

def DELETE_EDGE(tree, st, ed):
    for i in range(len(tree)):
        if st == tree[i][0] and ed == tree[i][1]:
            del tree[i]
            break

    for i in range(len(tree)):
        if st == tree[i][1] and ed == tree[i][0]:
            del tree[i]
            break

def ADD_EDGE(tree, st, ed, dist):
    tree.append((st, ed, dist))
    tree.append((ed, st, dist))

def GET_DIST(tree, st, ed):
    for i in range(len(tree)):
        if st == tree[i][0] and ed == tree[i][1]:
            break

    return tree[i][2]

def GET_NEW_NUM(tree):
    max_num = 0
    for i in range(len(tree)):
        max_num = max(max_num, tree[i][0], tree[i][1])
    
    return max_num + 1

def ADD_LAYOVER(tree, st, ed, dist):
    global maxnode
    #layover = GET_NEW_NUM(tree)
    ADD_EDGE(tree, st, maxnode, dist)
    ADD_EDGE(tree, maxnode, ed, GET_DIST(tree, st, ed) - dist)
    DELETE_EDGE(tree, st, ed)
    maxnode += 1

def LIMBLENGTH(i, matDist):
    temp = []
    for j in range(len(matDist)):
        if i == j: continue
        for k in range(len(matDist)):
            if i == k or j == k: continue
            dist = matDist[i][j] + matDist[i][k] - matDist[j][k]
            temp.append(int(dist/2))
    
    return min(temp)

def FIND_INK(n, matDist):
    temp = []
    for i in range(len(matDist)):
        if i == n: continue
        for k in range(len(matDist)):
            if i == k or n == k: continue
            if matDist[i][n] + matDist[n][k] == matDist[i][k]:
                temp.append((i,n,k))
    return temp[0]

def TRIM(n, matDist):
    return [matDist[i][:n] for i in range(n)]

def ADDITIVE_PHYLOGENY(n, matDist):
    global maxnode

    PRINT_MATRIX(matDist, True)
    _n = n - 1
    if n == 2:
        tree = []
        ADD_EDGE(tree, 0, 1, matDist[0][1])
        return tree

    limb = LIMBLENGTH(_n, matDist)
    for i in range(_n):
        matDist[i][_n] -= limb
        matDist[_n][i] = matDist[i][_n]
    PRINT_MATRIX(matDist, True)
    
    i, _, k = FIND_INK(_n, matDist)
    print(i, _n, k)
    x = matDist[i][_n]
    
    matDist = TRIM(_n, matDist)

    PRINT_MATRIX(matDist, True)
    tree = ADDITIVE_PHYLOGENY(n-1, matDist)

    ADD_EDGE(tree, maxnode, _n, limb)
    ADD_LAYOVER(tree, i, k, x)
    

    return tree

n, matDist = PARSE(sInput)
PRINT_MATRIX(matDist)
maxnode = n
Tree = ADDITIVE_PHYLOGENY(n, matDist)
PRINT_TREE(Tree)