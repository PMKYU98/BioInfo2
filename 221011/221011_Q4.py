sInput1 = '''
4
0   20  17  11
20  0   20  13
17  20  0   10
11  13  10  0
'''

sInput2 = '''
27
0 558 767 179 821 142 317 535 297 834 675 450 808 729 586 792 292 51 101 67 122 900 257 500 569 88 442
558 0 119 623 974 855 389 185 548 361 266 636 284 958 635 255 372 640 128 718 64 619 752 846 105 927 995
767 119 0 982 176 433 684 903 547 744 585 369 795 309 510 734 594 581 695 845 172 247 391 521 299 220 610
179 623 982 0 170 79 302 613 566 494 330 649 210 819 826 413 544 322 951 488 572 705 476 560 192 377 955
821 974 176 170 0 909 608 50 954 103 202 52 378 645 357 733 262 412 897 551 181 787 672 611 854 591 699
142 855 433 79 909 0 781 491 132 394 972 203 789 782 168 597 643 756 835 797 435 133 520 763 54 910 768
317 389 684 302 608 781 0 757 77 353 667 946 209 321 908 90 499 719 151 99 221 419 334 485 741 701 936
535 185 903 613 50 491 757 0 350 971 337 131 525 754 235 347 349 264 959 704 549 860 466 364 721 546 356
297 548 547 566 954 132 77 350 0 254 314 573 447 376 671 94 858 748 702 303 561 401 824 56 617 218 916
834 361 744 494 103 394 353 971 254 0 290 523 420 968 664 116 440 543 931 312 265 990 204 944 938 930 657
675 266 585 330 202 972 667 337 314 290 0 755 791 346 899 578 336 234 921 524 539 928 503 315 999 711 467
450 636 369 649 52 203 946 131 573 523 755 0 989 189 198 518 737 126 139 287 432 891 324 462 143 227 765
808 284 795 210 378 789 209 525 447 420 791 989 0 565 456 790 138 785 874 917 60 289 725 934 121 1000 817
729 958 309 819 645 782 321 754 376 968 346 189 565 0 519 245 552 694 81 877 678 842 215 751 300 57 277
586 635 510 826 357 168 908 235 671 664 899 198 456 519 0 393 600 911 276 844 894 590 478 71 532 631 550
792 255 734 413 733 597 90 347 94 116 578 518 790 245 393 0 697 761 461 490 464 967 459 501 448 832 624
292 372 594 544 262 643 499 349 858 440 336 737 138 552 600 697 0 508 316 166 820 871 288 584 130 301 477
51 640 581 322 412 756 719 264 748 543 234 126 785 694 911 761 508 0 230 576 919 775 425 801 985 626 814
101 128 695 951 897 835 151 959 702 931 921 139 874 81 276 461 316 230 0 282 713 238 137 913 239 682 592
67 718 845 488 551 797 99 704 303 312 524 287 917 877 844 490 166 576 282 0 406 91 637 177 969 162 326
122 64 172 572 181 435 221 549 561 265 539 432 60 678 894 464 820 919 713 406 0 807 106 522 258 847 123
900 619 247 705 787 133 419 860 401 990 928 891 289 842 590 967 871 775 238 91 807 0 964 368 455 320 457
257 752 391 476 672 520 334 466 824 204 503 324 725 215 478 459 288 425 137 637 106 964 0 882 451 559 716
500 846 521 560 611 763 485 364 56 944 315 462 934 751 71 501 584 801 913 177 522 368 882 0 598 601 184
569 105 299 192 854 54 741 721 617 938 999 143 121 300 532 448 130 985 239 969 258 455 451 598 0 207 630
88 927 220 377 591 910 701 546 218 930 711 227 1000 57 631 832 301 626 682 162 847 320 559 601 207 0 984
442 995 610 955 699 768 936 356 916 657 467 765 817 277 550 624 477 814 592 326 123 457 716 184 630 984 0
'''

sInput = sInput2
INF = 0

def PRINT_TREE(tree):
    for edge in sorted(tree):
        print('%d->%d:%.3f' % (edge[0], edge[1], edge[2]))

def WRITE_TREE(tree):
    temp = []
    for edge in sorted(tree):
        temp.append('%d->%d:%.3f' % (edge[0], edge[1], edge[2]))

    temp = '\n'.join(temp)
    with open('221011/221011_Q4_output.txt', 'w') as f:
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

def PRINT_MATRIX(mat, newline=False):
    if newline: print('')
    for l in mat:
        print('\t'.join(['%.3f' % i for i in l]))

def PARSE(sInput):
    global INF

    lines = sInput.strip().split('\n')
    n = int(lines[0])

    matDist = []
    for l in lines[1:]:
        temp = [int(x) for x in l.split(' ') if x != '']
        matDist.append(temp)
        INF = max(INF, max(temp))

    return n, matDist

def INITIALIZE(n):
    lstClstrs = [i for i in range(n)]
    dirAge = {}
    for i in range(len(lstClstrs)):
        dirAge[lstClstrs[i]] = 0
    dirChildren = {}
    return lstClstrs, dirAge, dirChildren

def FIND_CLOSEST(matDist):
    minimum = INF
    minY,minX = len(matDist), len(matDist)
    for i in range(len(matDist)):
        for j in range(len(matDist[i])):
            if i == j: continue
            if minimum > matDist[i][j]:
                minimum = matDist[i][j]
                minY, minX = i, j

    return minY, minX

def PROPORTION(v):
    global dirChildren

    sum = 0
    if v in dirChildren:
        for child in dirChildren[v]:
            sum += PROPORTION(child)
    else:
        sum += 1
    
    return sum

def MERGE_DIST(i, j, matDist):
    global lstClstrs, dirChildren

    y1, y2, x1, x2 = i, j, i, j
    prop_i, prop_j = PROPORTION(lstClstrs[i]), PROPORTION(lstClstrs[j])
    age = matDist[i][j] / 2

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

    new = max(lstClstrs) + 1
    temp = []
    for idx in range(len(lstClstrs)):
        if idx == i: temp.append(new)
        elif idx == j: continue
        else: temp.append(lstClstrs[idx])

    dirChildren[new] = (lstClstrs[i], lstClstrs[j])
    lstClstrs = temp
    dirAge[new] = age
    

    return matDist 

def UPGMA(n, matDist):
    global lstClstrs, dirChildren

    tree = []
    while(len(lstClstrs) > 1):
        minY, minX = FIND_CLOSEST(matDist)
        matDist = MERGE_DIST(minY, minX, matDist)

    for key in dirChildren:
        for child in dirChildren[key]:
            ADD_EDGE(tree, key, child, dirAge[key] - dirAge[child])

    return tree


n, matDist = PARSE(sInput)

lstClstrs, dirAge, dirChildren = INITIALIZE(n)

Tree = UPGMA(n, matDist)
PRINT_TREE(Tree)