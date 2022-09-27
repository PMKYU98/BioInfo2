sInput= '''
0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3
'''


class Queue:
    def __init__(self):
        self.list = []

    def add_element(self, u, longest):
        templist = self.list
        tempnode = [tup[0] for tup in templist]
        if u in tempnode: 
        

class Graph:
    def __init__(self, ed):
        self.visited = [True for i in range(ed + 1)]
        self.next = [[] for i in range(ed + 1)]
        self.edges = []
        self.longest = [0 for i in range(ed + 1)]

        self.queue = Queue()

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
        self.next[u].append(v)


def PARSE(s):
    lines = s.strip().split('\n')
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
    graph.add_edge(edge[0], edge[1], edge[2])

print(graph.next)
print(graph.edges)
print(graph.visited)