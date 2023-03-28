import sys
from collections import defaultdict, deque

edges=defaultdict(list)
n, m, s=map(int, sys.stdin.readline().split())
for _ in range(m):
    u, v= map(int, sys.stdin.readline().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

for k in edges:
    edges[k].sort()

def bfs(s):
    q=deque(); visited=[0 for i in range(n)]
    q.append(s); visited[s]=1
    while q:
        u=q.popleft()
        print(u+1, end=" ")
        for v in edges[u]:
            if not visited[v]:
                visited[v]=1
                q.append(v)

def dfs(s, visited):
    visited[s]=1
    print(s+1, end=" ")
    for v in edges[s]:
        if not visited[v]:
            dfs(v, visited)

dfs(s-1, [0 for i in range(n)])
print()
bfs(s-1)
