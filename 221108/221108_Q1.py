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

def PRINT_POINTS(points):
    m = len(points[0])
    string = ' '.join(['%.1f'] * m)
    for point in points:
        loc = ['%.3f' % x for x in point]
        string = ' '.join(loc)
        print(string)

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

def HIDDEN_MATRIX(beta, lCenters, lPoints):
    tempHidden = []
    for i in range(len(lCenters)):
        rowHidden = []
        center = lCenters[i]
        for j in range(len(lPoints)):
            data = lPoints[j]
            value = 1 / math.exp(beta * DIST(data, center))
            rowHidden.append(value)

        tempHidden.append(rowHidden)
    
    rowSum = []
    for j in range(len(lPoints)):
        temp = 0
        for i in range(len(lCenters)):
            temp += tempHidden[i][j]
        rowSum.append(temp)
    
    matHidden = []
    for i in range(len(lCenters)):
        temp = [tempHidden[i][j] / rowSum[j] for j in range(len(lPoints))]
        matHidden.append(temp)

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
        
        lCenters = lCenters_new

    return lCenters
            

inputfile = '221108/221108_Q1_input3.txt'

k, beta, lPoints = PARSE(inputfile)
lCenters = SOFT_KMEANS(k, beta, 100, lPoints)
PRINT_POINTS(lCenters)