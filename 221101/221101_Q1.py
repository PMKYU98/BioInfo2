import math

def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        lines = f.readlines()
        k, m = [int(x) for x in lines[0].strip().split(delimiter)]

    points = []
    for point in lines[1:]:
        l = point.strip().split(delimiter)
        pos = [float(x) for x in l]
        points.append(pos)

    return k, m, points

def PRINT_CENTERS(m, centers):
    global points

    string = ' '.join(['%.1f'] * m)
    for center in centers:
        loc = ['%.1f' % x for x in points[center]]
        string = ' '.join(loc)
        print(string)

def DIST(v, w):
    global points

    pos1 = points[v]
    pos2 = points[w]

    temp = 0
    for x1, x2 in zip(pos1, pos2):
        temp += (x1 - x2) ** 2
    
    return math.sqrt(temp)

def MIN_DIST(v, centers):
    return min([DIST(v, center) for center in centers])

def FIND_NEXT_CENTER(centers):
    global points 

    dists = [MIN_DIST(point, centers) for point in range(len(points))]
    max_dist = max(dists)
    max_v = dists.index(max_dist)

    temp = dists
    while max_v in centers:
        temp.remove(max_dist)
        max_dist = max(temp)
        max_v = dists.index(max_dist)

    return max_v

def FFT(k):
    global points

    centers = [0]
    while len(centers) < k:
        next_center = FIND_NEXT_CENTER(centers)
        centers.append(next_center)

    return centers


inputfile = '221101/221101_Q1_input3.txt'
k, m, points = PARSE(inputfile)
centers = FFT(k)
PRINT_CENTERS(m, centers)
