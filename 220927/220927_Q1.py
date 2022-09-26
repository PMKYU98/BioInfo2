sInput= '''
0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3
'''


class Node():
    def __init__(self, num):
        self._num = num
        self._next = []

    def add_next(self, v, l):
        self._next.append((v, l))

class Graph():
    def __init__(self, ed):
        self.nodes = []
        for i in range(ed+1):
            self.nodes.append(Node(i))

    def traverse(self):
        ways = []


def PARSE(s):
    lines = sInput.strip().split('\n')
    st = int(lines[0])
    ed = int(lines[1])
    edges = []
    for l in lines[2:]:
        _l = l.split(':')
        weight = int(_l[1])
        _l = _l[0].split('->')
        u, v = int(_l[0]), int(_l[1])
        edges.append((u, v, weight))

    return st, ed, edges

st, ed, edges = PARSE(sInput)
graph = Graph(ed)

for edge in edges:
    graph.nodes[edge[0]].add_next(edge[1], edge[2])

print(graph.nodes[1]._next)