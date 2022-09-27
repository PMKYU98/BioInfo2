sInput= '''
0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3
'''

class Graph:
    def __init__(self, n):
        self.n = n
        self.next = [[] for _ in range(self.n)]
        self.before = [[] for _ in range(self.n)]
        self.visited = [False for _ in range(self.n)]
        self.longest = [0 for _ in range(self.n)]

    def check(self):
        print(self.longest)

    def add_edge(self, u, v, w):
        self.next[u].append((v, w))
        self.before[v].append((u, w))

    def search(self, u, d):
        self.check()
        print(self.next[u])
        for v, w in self.next[u]:
            self.longest[v] = max(self.longest[v], d + w)
            self.search(v, d + w)
            
    def tour(self, st):
        self.search(st, 0)

    def backtour(self, st, ed):
        answer = []
        
        current = ed
        while True:
            answer.append(current)
            if current == st: break
            for v, w in self.before[current]:
                if self.longest[v] == self.longest[current] - w:
                    current = v

        print('->'.join([str(i) for i in reversed(answer)]))
            



def PARSE(s):
    lines = s.strip().split('\n')
    st = int(lines[0])
    ed = int(lines[1])
    n = 0
    edges = []
    for l in lines[2:]:
        _l = l.split(':')
        weight = int(_l[1])
        _l = _l[0].split('->')
        u, v = int(_l[0]), int(_l[1])
        if u >= n: n = u
        if v >= n: n = v
        edges.append((u, v, weight))

    return n + 1, st, ed, edges

n, st, ed, edges = PARSE(sInput)
graph = Graph(n)

for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2])

print(graph.next)
graph.tour(st)
graph.backtour(st, ed)
