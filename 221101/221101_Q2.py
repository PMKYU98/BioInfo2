import math

def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        lines = f.readlines()
        k, m = [int(x) for x in lines[0].strip().split(delimiter)]

    centers =[]
    for center in lines[1:1+k]:
        l = center.strip().split(delimiter)
        pos = [float(x) for x in l]
        centers.append(pos)

    points = []
    for point in lines[1+k+1:]:
        l = point.strip().split(delimiter)
        pos = [float(x) for x in l]
        points.append(pos)

    return k, m, centers, points

def DIST(v, w):
    temp = 0
    for x1, x2 in zip(v, w):
        temp += (x1 - x2) ** 2
    
    return math.sqrt(temp)

def NEAREST_CENTER_DIST(v, centers):
    return min([DIST(v, center) for center in centers])

def DISTORTION(centers):
    global points

    temp = 0
    for point in points:
        temp += NEAREST_CENTER_DIST(point, centers) ** 2
    
    return temp / len(points)


inputfile = '221101/221101_Q2_input3.txt'
k, m, centers, points = PARSE(inputfile)
print('%.3f' % DISTORTION(centers))
