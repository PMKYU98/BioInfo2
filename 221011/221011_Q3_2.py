sInput1 = '''
4
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''

sInput2 = '''
29
0 3036 4777 1541 2766 6656 2401 4119 7488 4929 5344 3516 1485 6392 2066 3216 7008 7206 1187 6491 3379 6262 6153 4927 6670 4997 9010 5793 9032
3036 0 6323 3087 4312 8202 1619 5665 9034 2205 6890 966 3031 7938 3612 492 4284 8752 2023 8037 4925 3538 3429 6473 3946 2273 10556 7339 10578
4777 6323 0 4054 2571 3455 5688 1972 4287 8216 2143 6803 4126 3191 3183 6503 10295 4005 4474 3290 2964 9549 9440 1726 9957 8284 5809 2592 5831
1541 3087 4054 0 2043 5933 2452 3396 6765 4980 4621 3567 890 5669 1343 3267 7059 6483 1238 5768 2656 6313 6204 4204 6721 5048 8287 5070 8309
2766 4312 2571 2043 0 4450 3677 1913 5282 6205 3138 4792 2115 4186 1172 4492 8284 5000 2463 4285 1173 7538 7429 2721 7946 6273 6804 3587 6826
6656 8202 3455 5933 4450 0 7567 3851 1082 10095 1872 8682 6005 1992 5062 8382 12174 800 6353 1047 4843 11428 11319 3053 11836 10163 2604 2545 2626
2401 1619 5688 2452 3677 7567 0 5030 8399 3512 6255 2099 2396 7303 2977 1799 5591 8117 1388 7402 4290 4845 4736 5838 5253 3580 9921 6704 9943
4119 5665 1972 3396 1913 3851 5030 0 4683 7558 2539 6145 3468 3587 2525 5845 9637 4401 3816 3686 2306 8891 8782 2122 9299 7626 6205 2988 6227
7488 9034 4287 6765 5282 1082 8399 4683 0 10927 2704 9514 6837 2824 5894 9214 13006 1172 7185 1879 5675 12260 12151 3885 12668 10995 2144 3377 2166
4929 2205 8216 4980 6205 10095 3512 7558 10927 0 8783 2859 4924 9831 5505 1891 3719 10645 3916 9930 6818 2973 2864 8366 3381 1708 12449 9232 12471
5344 6890 2143 4621 3138 1872 6255 2539 2704 8783 0 7370 4693 1608 3750 7070 10862 2422 5041 1707 3531 10116 10007 1741 10524 8851 4226 1233 4248
3516 966 6803 3567 4792 8682 2099 6145 9514 2859 7370 0 3511 8418 4092 1146 4938 9232 2503 8517 5405 4192 4083 6953 4600 2927 11036 7819 11058
1485 3031 4126 890 2115 6005 2396 3468 6837 4924 4693 3511 0 5741 1415 3211 7003 6555 1182 5840 2728 6257 6148 4276 6665 4992 8359 5142 8381
6392 7938 3191 5669 4186 1992 7303 3587 2824 9831 1608 8418 5741 0 4798 8118 11910 2542 6089 1827 4579 11164 11055 2789 11572 9899 4346 2281 4368
2066 3612 3183 1343 1172 5062 2977 2525 5894 5505 3750 4092 1415 4798 0 3792 7584 5612 1763 4897 1785 6838 6729 3333 7246 5573 7416 4199 7438
3216 492 6503 3267 4492 8382 1799 5845 9214 1891 7070 1146 3211 8118 3792 0 3970 8932 2203 8217 5105 3224 3115 6653 3632 1959 10736 7519 10758
7008 4284 10295 7059 8284 12174 5591 9637 13006 3719 10862 4938 7003 11910 7584 3970 0 12724 5995 12009 8897 1442 2699 10445 1088 3447 14528 11311 14550
7206 8752 4005 6483 5000 800 8117 4401 1172 10645 2422 9232 6555 2542 5612 8932 12724 0 6903 1597 5393 11978 11869 3603 12386 10713 2694 3095 2716
1187 2023 4474 1238 2463 6353 1388 3816 7185 3916 5041 2503 1182 6089 1763 2203 5995 6903 0 6188 3076 5249 5140 4624 5657 3984 8707 5490 8729
6491 8037 3290 5768 4285 1047 7402 3686 1879 9930 1707 8517 5840 1827 4897 8217 12009 1597 6188 0 4678 11263 11154 2888 11671 9998 3401 2380 3423
3379 4925 2964 2656 1173 4843 4290 2306 5675 6818 3531 5405 2728 4579 1785 5105 8897 5393 3076 4678 0 8151 8042 3114 8559 6886 7197 3980 7219
6262 3538 9549 6313 7538 11428 4845 8891 12260 2973 10116 4192 6257 11164 6838 3224 1442 11978 5249 11263 8151 0 1953 9699 1104 2701 13782 10565 13804
6153 3429 9440 6204 7429 11319 4736 8782 12151 2864 10007 4083 6148 11055 6729 3115 2699 11869 5140 11154 8042 1953 0 9590 2361 2592 13673 10456 13695
4927 6473 1726 4204 2721 3053 5838 2122 3885 8366 1741 6953 4276 2789 3333 6653 10445 3603 4624 2888 3114 9699 9590 0 10107 8434 5407 2190 5429
6670 3946 9957 6721 7946 11836 5253 9299 12668 3381 10524 4600 6665 11572 7246 3632 1088 12386 5657 11671 8559 1104 2361 10107 0 3109 14190 10973 14212
4997 2273 8284 5048 6273 10163 3580 7626 10995 1708 8851 2927 4992 9899 5573 1959 3447 10713 3984 9998 6886 2701 2592 8434 3109 0 12517 9300 12539
9010 10556 5809 8287 6804 2604 9921 6205 2144 12449 4226 11036 8359 4346 7416 10736 14528 2694 8707 3401 7197 13782 13673 5407 14190 12517 0 4899 1758
5793 7339 2592 5070 3587 2545 6704 2988 3377 9232 1233 7819 5142 2281 4199 7519 11311 3095 5490 2380 3980 10565 10456 2190 10973 9300 4899 0 4921
9032 10578 5831 8309 6826 2626 9943 6227 2166 12471 4248 11058 8381 4368 7438 10758 14550 2716 8729 3423 7219 13804 13695 5429 14212 12539 1758 4921 0 
'''

sInput = sInput2

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