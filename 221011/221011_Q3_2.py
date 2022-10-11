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
    for edge in sorted(tree):
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

def GET_PATH(tree, st, ed, visited):
    visited[st] = True
    next_v = [edge[1] for edge in tree if edge[0] == st]
    for v in next_v:
        if visited[v] == True: continue
        if v == ed: return [st, ed]

        return [st] + GET_PATH(tree, v, ed, visited)

def PLACE_LAYOVER(tree, st, ed, dist):
    path = GET_PATH(tree, st, ed, [False for _ in range(maxnode)])

    stack = 0
    for i in range(1, len(path)):
        if stack + GET_DIST(tree, path[i-1], path[i]) >= dist:
            break
        stack += GET_DIST(tree, path[i-1], path[i])
    return path[i-1], path[i], dist - stack

def ADD_LAYOVER(tree, st, ed, dist):
    global maxnode
    
    v, w, d = PLACE_LAYOVER(tree, st, ed, dist)
    ADD_EDGE(tree, v, maxnode, d)
    ADD_EDGE(tree, maxnode, w, GET_DIST(tree, v, w) - d)
    DELETE_EDGE(tree, v, w)
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
    _n = n - 1
    if n == 2:
        tree = []
        ADD_EDGE(tree, 0, 1, matDist[0][1])
        return tree

    limb = LIMBLENGTH(_n, matDist)
    for i in range(_n):
        matDist[i][_n] -= limb
        matDist[_n][i] = matDist[i][_n]

    i, _, k = FIND_INK(_n, matDist)
    x = matDist[i][_n]
    
    matDist = TRIM(_n, matDist)

    tree = ADDITIVE_PHYLOGENY(n-1, matDist)

    ADD_EDGE(tree, maxnode, _n, limb)
    ADD_LAYOVER(tree, i, k, x)
    
    return tree

n, matDist = PARSE(sInput)
maxnode = n
Tree = ADDITIVE_PHYLOGENY(n, matDist)
PRINT_TREE(Tree)