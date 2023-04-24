import sys
from collections import defaultdict

def dfs(s, e, d):
    if s==e:
        return 
    for k, v in edges[s].items():
        if not visit[k]:
            visit[k]=d+v
            dfs(k, e, d+v)

edges=defaultdict(dict)
n, m=map(int, sys.stdin.readline().split())
visit=[[0 for _ in range(n)] for _ in range(n)]
for i in range(1, n):
    x, y, d=map(int, sys.stdin.readline().split())
    edges[x-1][y-1]=d
    edges[y-1][x-1]=d

for _ in range(m):
    x, y=map(int, sys.stdin.readline().split())
    visit=[0 for _ in range(n)]
    visit[x-1]=1
    dfs(x-1, y-1, 0)
    print(visit[y-1])