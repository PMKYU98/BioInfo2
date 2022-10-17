sInput1 = '''
4
4->CAAATCCC
4->ATTGCGAC
5->CTGCGCTG
5->ATGGACGA
6->4
6->5
'''

sInput = sInput1
BASES = ['A', 'C', 'G', 'T']
INF = 999

def HAMMING(s1, s2):
    score = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: score += 1
    return score

def PRINT_TREE(tree):
    for edge in tree:
        print('%s->%s:%d' % (edge[0], edge[1], edge[2]))

def ADD_EDGE(tree, st, ed, dist):
    tree.append((st, ed, dist))
    tree.append((ed, st, dist))

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])
    root = 0

    lstLeaves = []
    dicChildren = {}
    for l in lines[1:]:
        parent, child = int(l.split('->')[0]), l.split('->')[1]
        dicChildren.setdefault(parent, [])
        root = max(root, parent)
        if child.isdigit():
            dicChildren[parent].append(int(child))
        else:
            new = len(lstLeaves)
            lstLeaves.append(child)
            dicChildren[int(parent)].append(new)
        
    return n, len(lstLeaves[0]), root, lstLeaves, dicChildren

def RIPE_NODE(visited):
    global dicChildren
    for parent in dicChildren:
        if visited[parent]: continue
        else:
            child0, child1 = dicChildren[parent]
            if visited[child0] and visited[child1]: return parent
    
    return None

def DELTA(c1, c2):
    if c1 == c2: return 0
    else: return 1

def MAKE_RIPE(c0Score, c1Score):
    score = {}
    backtrack = {}

    for base in BASES:
        c0Scoremin, c0Basemin = INF, 'X'
        for c0base in c0Score:
            temp = c0Score[c0base] + DELTA(base, c0base)
            if temp < c0Scoremin: c0Scoremin, c0Basemin = temp, c0base

        c1Scoremin, c1Basemin = INF, 'X'
        for c1base in c1Score:
            temp = c1Score[c1base] + DELTA(base, c1base)
            if temp < c1Scoremin: c1Scoremin, c1Basemin = temp, c1base

        score[base] = c0Scoremin + c1Scoremin
        backtrack[base] = (c0Basemin, c1Basemin)
        
    return score, backtrack
        


def SMALL_PARSIMONY_CHAR(n, root, lstChar):
    visited = [False for _ in range(root+1)]
    
    dicScores = {}
    dicBacktrack = {}
    for node in range(root+1):
        dicScores.setdefault(node, {})
        if node < n:
            visited[node] = True
            for base in BASES:
                if lstChar[node] == base: dicScores[node][base] = 0
                else: dicScores[node][base] = INF
            dicBacktrack[node] = None
    
    while True:
        v = RIPE_NODE(visited)
        if v is None: break
        visited[v] = True

        dicScores[v], dicBacktrack[v] = MAKE_RIPE(dicScores[dicChildren[v][0]], dicScores[dicChildren[v][1]])

    return dicScores, dicBacktrack

def BACKTRACK(node, char, dicBacktrack, dicChar={}):
    global dicChildren

    dicChar[node] = char
    if node in dicChildren:
        child0, child1 = dicChildren[node]
        dicChar = BACKTRACK(child0, dicBacktrack[node][char][0], dicBacktrack, dicChar)
        dicChar = BACKTRACK(child1, dicBacktrack[node][char][1], dicBacktrack, dicChar)
    
    return dicChar

def TREE_CONSTRUCTION(node, dicString, tree):
    global dicChildren

    if node in dicChildren:
        sNode = dicString[node]
        child0, child1 = dicChildren[node]
        sChild0 = dicString[child0]
        sChild1 = dicString[child1]

        tree = TREE_CONSTRUCTION(child0, dicString, tree)
        tree = TREE_CONSTRUCTION(child0, dicString, tree)
        ADD_EDGE(tree, sNode, sChild0, HAMMING(sNode, sChild0))
        ADD_EDGE(tree, sNode, sChild1, HAMMING(sNode, sChild1))

    return tree


def SMALL_PARSIMONY(n, root):
    global lstLeaves

    dicString = {}
    finalscore = 0
    for node in range(root+1):
        dicString[node] = []
    
    for m in range(len(lstLeaves[0])):
        dicScores, dicBacktrack = SMALL_PARSIMONY_CHAR(n, root, [leave[m] for leave in lstLeaves])
        temp = BACKTRACK(root, min(dicScores[root], key=dicScores[root].get), dicBacktrack, {})
        finalscore += min(dicScores[root].values())

        for node in temp:
            dicString[node].append(temp[node])

    for k in dicString:
        dicString[k]= ''.join(dicString[k])

    tree = TREE_CONSTRUCTION(root, dicString, [])

    return finalscore, dicString, tree
        

n, m, root, lstLeaves, dicChildren = PARSE(sInput)
print('n: %d, m: %d, root: %d' % (n, m, root))
print(lstLeaves)
print(dicChildren)

finalscore, dicString, tree = SMALL_PARSIMONY(n, root)
print(finalscore)
for k in dicString:
    print('%d: %s' % (k, dicString[k]))
print(tree)
PRINT_TREE(tree)