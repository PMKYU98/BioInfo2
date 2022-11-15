MAXNODE = 0

def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()

    return sInput

def PRINT_TREE(Tree):
    for edge in Tree:
        print('%d->%d:%s' % (edge[0], edge[1], edge[2]))

def PRINT_EDGES(Tree):
    for edge in Tree:
        print(edge[2])

def READ_EDGE(v, w, Tree):
    for edge in Tree:
        if edge[0] != v: continue
        if edge[1] != w: continue
        return edge[2]

def ADD_EDGE(v, w, label, Tree, dicChildren):
    Tree.append((v, w, label))
    dicChildren.setdefault(v, [])
    dicChildren[v].append(w)

    return Tree, dicChildren

def DELETE_EDGE(v, w, Tree, dicChildren):
    edge = (v, w, READ_EDGE(v, w, Tree))
    Tree.remove(edge)
    dicChildren[v].remove(w)

    return Tree, dicChildren

def FIND_PARENT(v, Tree):
    for edge in Tree:
        if edge[1] == v: return edge[0]

def ADD_ALL(string, current, Tree, dicChildren):
    global MAXNODE
    for new_char in string:
        MAXNODE += 1
        ADD_EDGE(current, MAXNODE, new_char, Tree, dicChildren)
        current = MAXNODE
    return Tree, dicChildren

def SUFFIX_TREE_HELPER(suffix, Tree, dicChildren):
    global MAXNODE
    current = 0
    idx = 0
    
    while current in dicChildren:
        descend = current
        for child in dicChildren[current]:
            if READ_EDGE(current, child, Tree) == suffix[idx]:
                descend = child

        if current != descend:
            current = descend
            idx += 1
        else:
            ADD_ALL(suffix[idx:], current, Tree, dicChildren)
            break

    return Tree, dicChildren
            
def SUFFIX_TREE(sInput):
    global MAXNODE
    Tree = []
    dicChildren = {}

    lSuffices = sorted([sInput[i:] for i in range(len(sInput))])
    print(lSuffices)
    Tree, dicChildren = ADD_EDGE(0, 1, lSuffices[0], Tree, dicChildren)
    MAXNODE = 1

    for suffix in lSuffices[1:]:
        Tree, dicChildren = SUFFIX_TREE_HELPER(suffix, Tree, dicChildren)

    return Tree, dicChildren

def FIND_NONBRANCHING(dicChildren):
    return [key for key in dicChildren if len(dicChildren[key]) == 1]

def PATH_HELPER(current, stack, nonbranching, dicChildren):
    _stack, _nonbranching = stack, nonbranching
    _stack.append(current)
    _nonbranching.remove(current)

    if current in dicChildren:
        child = dicChildren[current][0]
        if child in _nonbranching:
            _stack, _nonbranching = PATH_HELPER(child, _stack, _nonbranching, dicChildren)
    
    return _stack, _nonbranching
        
def PATH_NONBRANCHING(nonbranching, dicChildren):
    lPaths = []
    while len(nonbranching) > 0:
        stack, nonbranching = PATH_HELPER(nonbranching[0], [], nonbranching, dicChildren)
        lPaths.append(stack)

    return lPaths

def MERGE_PATH(lPaths, Tree, dicChildren):
    for path in lPaths:
        st, ed = path[0], path[-1]
        before_st = FIND_PARENT(st, Tree)
        after_ed = dicChildren[ed][0]

        new_edge = [READ_EDGE(before_st, st, Tree)]
        for i in range(len(path)):
            if i == len(path) - 1: break
            new_edge.append(READ_EDGE(path[i], path[i+1], Tree))
            Tree, dicChildren = DELETE_EDGE(path[i], path[i+1], Tree, dicChildren)
        
        new_edge.append(READ_EDGE(ed, after_ed, Tree))
        Tree, dicChildren = ADD_EDGE(before_st, after_ed, ''.join(new_edge), Tree, dicChildren)
        Tree, dicChildren = DELETE_EDGE(before_st, st, Tree, dicChildren)
        Tree, dicChildren = DELETE_EDGE(ed, after_ed, Tree, dicChildren)

    return Tree, dicChildren


inputfile = '221115/221115_Q1_input1.txt'
sInput = PARSE(inputfile)
Tree, dicChildren = SUFFIX_TREE(sInput)
#PRINT_TREE(Tree)
nonbranching = FIND_NONBRANCHING(dicChildren)
lPaths = PATH_NONBRANCHING(nonbranching, dicChildren)
Tree, dicChildren = MERGE_PATH(lPaths, Tree, dicChildren)
PRINT_EDGES(Tree)
