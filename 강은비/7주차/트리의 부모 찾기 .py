import sys
from collections import deque, defaultdict

n=int(sys.stdin.readline())
edges=defaultdict(list)

for _ in range(n-1):
    x, y=map(int, sys.stdin.readline().split())
    edges[x].append(y)
    edges[y].append(x)

nodes=[0]*(n+1)  #노드의 부모 저장
nodes[1]=-1
l=deque([1]) #root -> 1

while l:
    x=l.popleft()
    for v in edges[x]:
        if not nodes[v]:
            l.append(v)
            nodes[v]=x
    
for x in nodes[2:]:
    print(x)

