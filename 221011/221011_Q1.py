sInput = '''
4
0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6
'''

def PRINT_MATRIX(matScore):
    for l in matScore:
        print('\t'.join([str(i) for i in l]))

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])
    max_node = 0

    dirAdj = {}
    for l in lines[1:]:
        temp = l.split(':')
        nodes, dist = temp[0], int(temp[1])

        temp = nodes.split('->')
        st, ed = int(temp[0]), int(temp[1])
        max_node = max(max_node, st)
        dirAdj.setdefault(st, {})
        dirAdj[st][ed] = dist

    return n, max_node, dirAdj

def INITIALIZE(max_node):
    x = max_node + 1
    matAdj = [[None] * x for _ in range(x)]
    for i in range(x):
        matAdj[i][i] = 0

    return matAdj

def DISTANCE(i, curr, j, stack, visited):
    global matAdj
    
    visited.append(curr)

    if curr == j: 
        matAdj[i][j] = stack
        matAdj[j][i] = stack
        return

    childs =  dirAdj[curr].keys()
    for child in childs:
        if matAdj[i][j] is not None: break
        if child not in visited:
            DISTANCE(i, child, j, stack + dirAdj[curr][child], visited)
    
def TRIM(matAdj, n):
    matAns = [matAdj[i][:n] for i in range(n)]
    return matAns


n, max_node, dirAdj = PARSE(sInput)
matAdj = INITIALIZE(max_node)

for i in range(max_node+1):
    for j in range(max_node+1):
        if matAdj[i][j] is None:
            DISTANCE(i,i,j,0,[])

matAns = TRIM(matAdj, n)
PRINT_MATRIX(matAns)
