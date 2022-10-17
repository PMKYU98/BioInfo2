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
A, C, G, T = 'A', 'C', 'G', 'T'
INF = 'INF'

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])
    root = 0

    lstLeaves = []
    dirChildren = {}
    for l in lines[1:]:
        parent, child = int(l.split('->')[0]), l.split('->')[1]
        dirChildren.setdefault(parent, [])
        root = max(root, parent)
        if child.isdigit():
            dirChildren[parent].append(int(child))
        else:
            new = len(lstLeaves)
            lstLeaves.append(child)
            dirChildren[int(parent)].append(new)
        
    return n, len(lstLeaves[0]), root, lstLeaves, dirChildren

def SMALL_PARSIMONY(n, root, idx):
    
         
    

n, m, root, lstLeaves, dirChildren = PARSE(sInput)
print('n: %d, m: %d, root: %d' % (n, m, root))
print(lstLeaves)
print(dirChildren)