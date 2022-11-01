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

def PRINT_CENTERS(centers):
    for center in centers:
        loc = ['%.3f' % x for x in center]
        print(' '.join(loc))

def DIST(v, w):
    temp = 0
    for x1, x2 in zip(v, w):
        temp += (x1 - x2) ** 2
    
    return math.sqrt(temp)

def NEAREST_CENTER(v, centers):
    temp = [DIST(v, center) for center in centers]
    return temp.index(min(temp))

def CHOOSE_CLUSTER(centers, points):
    clusters = [[] for _ in centers]
    for point in points:
        clusters[NEAREST_CENTER(point, centers)].append(point)

    return clusters

def CENTER_OF_GRAVITY(cluster):
    center = []
    for dim in range(len(cluster[0])):
        temp = 0
        for point in cluster:
            temp += point[dim]
        center.append(temp / len(cluster))
    
    return center

def CONVERGED(centers1, centers2):
    return sorted(centers1) == sorted(centers2)

def LLOYD(centers, points):    
    while True:
        clusters = CHOOSE_CLUSTER(centers, points)
        new_centers = [CENTER_OF_GRAVITY(cluster) for cluster in clusters]
        if CONVERGED(centers, new_centers): break
        else: centers = new_centers

    return new_centers


inputfile = '221101/221101_Q3_input3.txt'
k, m, points = PARSE(inputfile)
centers = LLOYD(points[:k], points)
PRINT_CENTERS(centers)