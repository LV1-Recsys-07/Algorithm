import sys
from collections import defaultdict

edges=defaultdict(list)
n=int(sys.stdin.readline())
for i in range(1, n):
    a, b=map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)
q=int(sys.stdin.readline())

for _ in range(q):
    t, k=map(int, sys.stdin.readline().split())
    if t==1:
        if len(edges[k])>=2:  #부모간선, 자식간선이 있는 경우 단절점. 리프노드나 루트노드는 단절점 x
            print("yes")
        else:
            print("no")
    if t==2:    #모든 간선이 단절선
        print("yes")
