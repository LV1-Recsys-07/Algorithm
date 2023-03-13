from collections import deque

N, M, V = map(int, input().split())

graph = {i: set() for i in range(1, N+1)} # set으로 하면 정렬 된 것 같이 보이는데 왜 안되는거지
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

for key, val in graph.items():
    graph[key] = sorted(val)

visited_dfs = [] # set으로 하면 정렬되는 것 같음
visited_bfs = []

def dfs(v, g):
    if v in visited_dfs:
        return
    visited_dfs.append(v)
    for w in g[v]:
        dfs(w, g)

def bfs(v, g):
    q = deque([v])
    visited_bfs.append(v)

    while q:
        w = q.popleft()
        for i in graph[w]:
            if i not in visited_bfs:
                q.append(i)
                visited_bfs.append(i)

dfs(V, graph)
bfs(V, graph)

for d in visited_dfs:
    print(d, end=" ")
print()
for b in visited_bfs:
    print(b, end=" ")
