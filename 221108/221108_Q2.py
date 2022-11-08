def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())

    tempDist = []
    for l in lines[1:]:
        temp = [float(x) for x in l.strip().split(delimiter)]
        tempDist.append(temp)
    
    return n, tempDist

def PRINT_MATRIX(mat, newline=False):
    if newline: print('')
    for l in mat:
        print('\t'.join(['%.2f' % i for i in l]))

def FIND_CLOSEST(matDist):
    minimum = -1
    minY,minX = len(matDist), len(matDist)
    for i in range(len(matDist)):
        for j in range(len(matDist[i])):
            if i == j: continue
            if minimum < 0 or minimum > matDist[i][j]:
                minimum = matDist[i][j]
                minY, minX = i, j

    return minY, minX

def PROPORTION(n, dicElements):
    summed = 0

    if n in dicElements:
        for child in dicElements[n]:
            c_summed = PROPORTION(child, dicElements)
            summed += c_summed
    else: 
        summed += 1

    return summed

def CLUSTER(n, dicElements):
    storage = []

    if n in dicElements:
        for child in dicElements[n]:
            c_storage = CLUSTER(child, dicElements)
            storage += c_storage
    else: 
        storage += [str(n+1)]

    return storage

def MERGE_DIST(i, j, lClusters, dicElements, matDist):
    y1, y2, x1, x2 = i, j, i, j
    prop_i, prop_j = PROPORTION(lClusters[i], dicElements), PROPORTION(lClusters[j], dicElements)

    column1 = [matDist[y][x1] * prop_i for y in range(len(matDist))]
    column2 = [matDist[y][x2] * prop_j for y in range(len(matDist))]
    newCol = []
    for y in range(len(column1)):
        if y == y1: newCol.append(0)
        elif y == y2: newCol.append(0)
        else: newCol.append((column1[y] + column2[y]) / (prop_i + prop_j))

    row1 = [matDist[y1][x] * prop_i for x in range(len(matDist))]
    row2 = [matDist[y2][x] * prop_j for x in range(len(matDist))]
    newRow = []
    for x in range(len(row1)):
        if x == x1: newRow.append(0)
        elif x == x2: continue
        else: newRow.append((row1[x] + row2[x]) / (prop_i + prop_j))

    temp = []
    for y in range(len(matDist)):
        if y == y1: temp.append(newRow)
        elif y == y2: continue
        else: 
            l = matDist[y]
            new_l = []
            for x in range(len(l)):
                if x == x1: 
                    new_l.append(newCol[y])
                elif x == x2: continue
                else:
                    new_l.append(l[x])
            temp.append(new_l)

    matDist = temp

    new = max(lClusters) + 1
    temp = []
    for idx in range(len(lClusters)):
        if idx == i: temp.append(new)
        elif idx == j: continue
        else: temp.append(lClusters[idx])

    dicElements[new] = (lClusters[i], lClusters[j])
    lClusters = temp
    
    print(' '.join(CLUSTER(new, dicElements)))
    return lClusters, dicElements, matDist 

def HIERARCHICAL_CLUSTERING(n, matDist):
    lClusters = [x for x in range(n)]
    dicElements = {}

    while len(lClusters) > 1:
        minY, minX = FIND_CLOSEST(matDist)
        lClusters, dicElements, matDist = MERGE_DIST(minY, minX, lClusters, dicElements, matDist)
        

inputfile = '221108/221108_Q2_input4.txt'
n, matDist = PARSE(inputfile)
HIERARCHICAL_CLUSTERING(n, matDist)
