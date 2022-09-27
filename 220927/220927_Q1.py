sInput= '''
7
17
3->18:28
3->11:34
11->18:23
3->14:23
3->16:22
8->16:22
10->17:30
10->14:37
9->19:2
15->19:23
0->13:0
5->10:37
8->18:33
5->14:3
0->14:20
6->7:13
0->18:23
2->4:30
1->5:26
2->19:25
1->4:33
1->8:2
12->16:18
1->2:1
8->19:37
1->17:12
1->15:3
1->12:35
1->13:27
4->9:33
1->11:12
9->14:37
9->15:38
0->11:17
6->16:35
0->9:1
3->6:13
2->14:7
0->2:28
1->19:36
0->6:24
0->5:32
1->3:29
4->19:31
4->18:5
4->17:26
4->16:23
7->15:21
16->19:22
7->12:2
7->13:16
13->17:20
5->18:30
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
        #self.check()
        #print(self.next[u])
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

        print(self.longest[ed])
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

graph.tour(st)
graph.backtour(st, ed)