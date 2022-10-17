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

sInput = sInput1

def PRINT_TREE(tree):
    for edge in sorted(tree):
        print('%d->%d:%.3f' % (edge[0], edge[1], edge[2]))

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
    global maxnode

def PRINT_MATRIX(mat, newline=False):
    if newline: print('')
    for l in mat:
        print('\t'.join([str(i) for i in l]))

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])

    matD = []
    for l in lines[1:]:
        matD.append([int(x) for x in l.split(' ') if x != ''])

    return n, matD

def TOTAL_DISTANCE(i, matD):
    return sum(matD[i])

def NEIGHBOR_MATRIX(n, matD):
    matDstar = []
    for i in range(len(matD)):
        totalDistance_i = TOTAL_DISTANCE(i, matD)
        newRow = []
        for j in range(len(matD[i])):
            if i == j: newRow.append(0)
            else: 
                totalDistance_j = TOTAL_DISTANCE(j, matD)
                newRow.append((n - 2) * matD[i][j] - totalDistance_i - totalDistance_j)
        matDstar.append(newRow)

    return matDstar

def FIND_MINPOS(mat):
    minValue, minY, minX = 0, 0, 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] < minValue:
                minValue, minY, minX = mat[i][j], i, j

    return minY, minX

def MERGE_IJ(i, j, matD):
    global lstClstrs, dirChildren

    matDnew = []
    for y in range(len(matD)):
        if y == i or y == j: continue
        else:
            newRow = [matD[y][x] for x in range(len(matD[y])) if x != i and x != j]
            newRow.append((matD[y][i] + matD[y][j] - matD[i][j]) / 2)
            matDnew.append(newRow)
    
    newRow = [matDnew[y][-1] for y in range(len(matDnew))] + [0]
    matDnew.append(newRow)
        
    new = max(lstClstrs) + 1
    temp = []
    for idx in range(len(lstClstrs)):
        if idx == i or idx == j: continue
        else: temp.append(lstClstrs[idx])
    temp.append(new)

    dirChildren[new] = (lstClstrs[i], lstClstrs[j])
    lstClstrs = temp

    return new, matDnew

def INITIALIZE(n):
    lstClstrs = [i for i in range(n)]
    dirChildren = {}
    dirLimb = {}
    return lstClstrs, dirChildren, dirLimb

def NEIGHBOR_JOINING(n, matD):
    global lstClstrs
    tree = []

    while len(lstClstrs) > 1:
        if len(lstClstrs) == 2:
            ADD_EDGE(tree, lstClstrs[0], lstClstrs[1], matD[0][1])
            return tree

        matDstar = NEIGHBOR_MATRIX(n, matD)
        minY, minX = FIND_MINPOS(matDstar)
        
        delta = (TOTAL_DISTANCE(minY, matD) - TOTAL_DISTANCE(minX, matD)) / (n - 2)
        i, j = lstClstrs[minY], lstClstrs[minX]
        limb_i = (matD[minY][minX] + delta) / 2
        limb_j = (matD[minY][minX] - delta) / 2

        newnode, matD = MERGE_IJ(minY, minX, matD)
        ADD_EDGE(tree, newnode, i, limb_i)
        ADD_EDGE(tree, newnode, j, limb_j)
        n -= 1

    return tree


            
n, matD = PARSE(sInput)
lstClstrs, dirChildren, dirLimb = INITIALIZE(n)
Tree = NEIGHBOR_JOINING(n, matD)
PRINT_TREE(Tree)