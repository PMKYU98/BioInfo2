sInput1 = '''
4
0   20  17  11
20  0   20  13
17  20  0   10
11  13  10  0
'''

sInput2 = '''
21
0	560	717	637	527	783	807	478	554	800	837	630	750	621	849	442	453	761	617	495	692	
560	0	656	612	873	880	882	544	653	843	579	536	787	662	474	557	487	523	507	670	854	
717	656	0	839	859	881	700	732	594	723	583	482	716	784	689	764	503	704	746	622	584	
637	612	839	0	634	540	505	765	805	608	720	775	445	461	710	493	454	758	818	515	565	
527	873	859	634	0	795	470	593	792	567	682	467	875	771	844	822	561	728	556	647	740	
783	880	881	540	795	0	607	578	624	623	687	486	597	500	860	476	846	599	766	739	460	
807	882	700	505	470	607	0	816	791	663	545	518	570	738	489	605	788	835	741	459	667	
478	544	732	765	593	578	816	0	468	858	558	799	595	678	596	855	549	642	852	733	585	
554	653	594	805	792	624	791	468	0	636	715	812	749	490	782	657	539	827	754	448	571	
800	843	723	608	567	623	663	858	636	0	866	528	529	629	462	829	564	512	685	455	786	
837	579	583	720	682	687	545	558	715	866	0	664	525	543	443	810	521	709	721	801	616	
630	536	482	775	467	486	518	799	812	528	664	0	466	778	777	492	825	471	811	609	674	
750	787	716	445	875	597	570	595	749	529	525	466	0	650	562	581	604	874	828	509	742	
621	662	784	461	771	500	738	678	490	629	543	778	650	0	566	817	820	475	646	773	601	
849	474	689	710	844	860	489	596	782	462	443	777	562	566	0	693	806	763	707	673	458	
442	557	764	493	822	476	605	855	657	829	810	492	581	817	693	0	802	851	821	863	668	
453	487	503	454	561	846	788	549	539	564	521	825	604	820	806	802	0	464	516	793	465	
761	523	704	758	728	599	835	642	827	512	709	471	874	475	763	851	464	0	676	857	838	
617	507	746	818	556	766	741	852	754	685	721	811	828	646	707	821	516	676	0	713	580	
495	670	622	515	647	739	459	733	448	455	801	609	509	773	673	863	793	857	713	0	789	
692	854	584	565	740	460	667	585	571	786	616	674	742	601	458	668	465	838	580	789	0	
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

def PARSE(sInput, delimiter=' '):
    global INF

    lines = sInput.strip().split('\n')
    n = int(lines[0])

    matDist = []
    for l in lines[1:]:
        temp = [int(x) for x in l.split(delimiter) if x != '']
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


n, matDist = PARSE(sInput, '\t')

lstClstrs, dirAge, dirChildren = INITIALIZE(n)

Tree = UPGMA(n, matDist)
PRINT_TREE(Tree)