sInput1 = '''
4
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''

sInput2 = '''
20
0 1781 1129 4916 3402 2507 2716 3114 1175 4460 3489 5573 5059 3217 3221 1319 3098 4470 2384 1606
1781 0 1100 6293 4779 3884 1773 4491 2552 3517 2546 4630 4116 4594 2278 964 4475 5847 1441 2983
1129 1100 0 5641 4127 3232 2035 3839 1900 3779 2808 4892 4378 3942 2540 638 3823 5195 1703 2331
4916 6293 5641 0 2330 3799 7228 2348 3897 8972 8001 10085 9571 1869 7733 5831 2744 1258 6896 4984
3402 4779 4127 2330 0 2285 5714 834 2383 7458 6487 8571 8057 631 6219 4317 1230 1884 5382 3470
2507 3884 3232 3799 2285 0 4819 1997 1488 6563 5592 7676 7162 2100 5324 3422 1981 3353 4487 2575
2716 1773 2035 7228 5714 4819 0 5426 3487 3516 2545 4629 4115 5529 2277 1899 5410 6782 1940 3918
3114 4491 3839 2348 834 1997 5426 0 2095 7170 6199 8283 7769 649 5931 4029 942 1902 5094 3182
1175 2552 1900 3897 2383 1488 3487 2095 0 5231 4260 6344 5830 2198 3992 2090 2079 3451 3155 1243
4460 3517 3779 8972 7458 6563 3516 7170 5231 0 2795 2317 1803 7273 1527 3643 7154 8526 3684 5662
3489 2546 2808 8001 6487 5592 2545 6199 4260 2795 0 3908 3394 6302 1556 2672 6183 7555 2713 4691
5573 4630 4892 10085 8571 7676 4629 8283 6344 2317 3908 0 1190 8386 2640 4756 8267 9639 4797 6775
5059 4116 4378 9571 8057 7162 4115 7769 5830 1803 3394 1190 0 7872 2126 4242 7753 9125 4283 6261
3217 4594 3942 1869 631 2100 5529 649 2198 7273 6302 8386 7872 0 6034 4132 1045 1423 5197 3285
3221 2278 2540 7733 6219 5324 2277 5931 3992 1527 1556 2640 2126 6034 0 2404 5915 7287 2445 4423
1319 964 638 5831 4317 3422 1899 4029 2090 3643 2672 4756 4242 4132 2404 0 4013 5385 1567 2521
3098 4475 3823 2744 1230 1981 5410 942 2079 7154 6183 8267 7753 1045 5915 4013 0 2298 5078 3166
4470 5847 5195 1258 1884 3353 6782 1902 3451 8526 7555 9639 9125 1423 7287 5385 2298 0 6450 4538
2384 1441 1703 6896 5382 4487 1940 5094 3155 3684 2713 4797 4283 5197 2445 1567 5078 6450 0 3586
1606 2983 2331 4984 3470 2575 3918 3182 1243 5662 4691 6775 6261 3285 4423 2521 3166 4538 3586 0'''

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

def WRITE_TREE(tree):
    temp = []
    for edge in sorted(tree):
        temp.append('%d->%d:%d' % (edge[0], edge[1], edge[2]))

    temp = '\n'.join(temp)
    with open('221011/221011_Q3_output.txt', 'w') as f:
        f.write(temp)
    
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

        path = GET_PATH(tree, v, ed, visited)
        if path is not None:
            return [st] + path

    return None

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
WRITE_TREE(Tree)