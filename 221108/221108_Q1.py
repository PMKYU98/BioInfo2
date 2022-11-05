import math
from pickletools import float8

def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        lines = f.readlines()
    
    k = int(lines[0].strip().split(delimiter)[0])
    beta = float(lines[1].strip())

    lPoints = []
    for point in lines[2:]:
        l = point.strip().split(delimiter)
        pos = [float(x) for x in l]
        lPoints.append(pos)

    return k, beta, lPoints

def DIST(v, w):
    temp = 0
    for x1, x2 in zip(v, w):
        temp += (x1 - x2) ** 2
    
    return math.sqrt(temp)

def DOT(array1, array2):
    temp = 0
    for e1, e2 in zip(array1, array2):
        temp += e1 * e2
    
    return temp

def NTH_COORD(n, lPoints):
    return [point[n] for point in lPoints]

def HIDDEN_MATRIX_HELPER(beta, center, lPoints):
    temp = [math.exp(-1 * beta * DIST(point, center)) for point in lPoints]
    denom = sum(temp)
    return [numer / denom for numer in temp]

def HIDDEN_MATRIX(beta, lCenters, lPoints):
    matHidden = [HIDDEN_MATRIX_HELPER(beta, center, lPoints) for center in lCenters]
    return matHidden

def SOFT_KMEANS(k, beta, iter, lPoints):
    lCenters = lPoints[:k]
    n = len(lPoints)
    m = len(lPoints[0])

    for _ in range(iter):
        matHidden = HIDDEN_MATRIX(beta, lCenters, lPoints)
        lCenters_new = []
        for i in range(k):
            rowHidden = matHidden[i]
            rowOne = [1] * n
            new_center = []
            for j in range(m):
                x_ij = DOT(rowHidden, NTH_COORD(j, lPoints)) / DOT(rowHidden, rowOne)
                new_center.append(x_ij)

            lCenters_new.append(new_center)

    return lCenters_new
            

inputfile = '221108/221108_Q1_input1.txt'

k, beta, lPoints = PARSE(inputfile)
matHidden = HIDDEN_MATRIX(beta, lPoints[:2], lPoints)
lCenters = SOFT_KMEANS(k, beta, 100, lPoints)
print(lCenters)
