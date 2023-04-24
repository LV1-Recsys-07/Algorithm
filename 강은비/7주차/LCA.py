import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def dfs(root, d):
    depth[root]=d
    visit[root]=1
    for v in edges[root]:
        if visit[v]:
            continue
        p[v]=root
        dfs(v, d+1)

def find(x, y):
    while depth[x]!=depth[y]:
        if depth[x]<depth[y]:
            y=p[y]
        else:
            x=p[x]
    while True:
        if x==y:
            return x
        x=p[x]
        y=p[y]
        

edges=defaultdict(list)
n=int(sys.stdin.readline())
for _ in range(n-1):
    x, y=map(int, sys.stdin.readline().split())
    edges[x].append(y)
    edges[y].append(x)
m=int(sys.stdin.readline())

depth=[0 for _ in range(n+1)]
p=[0 for _ in range(n+1)]
visit=[0 for _ in range(n+1)]
dfs(1, 0)

for _ in range(m):
    x, y=map(int, sys.stdin.readline().split())
    print(find(x, y))
    
    
    