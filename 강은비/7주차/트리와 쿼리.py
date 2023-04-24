import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def maketree(node, p):
    for v in edges[node]:
        if v!=p:
            tree[node].append(v)
            maketree(v, node)

def checkchild(node):   #자식 개수 
    if node not in tree:
        return 0
    
    num[node]=len(tree[node])
    for v in tree[node]:
        num[node]+=checkchild(v)
    return num[node]

edges=defaultdict(list)
n, r, q=map(int, sys.stdin.readline().split())
for _ in range(n-1):
    u, v=map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)
tree=defaultdict(list)
num=[0 for _ in range(n+1)]

maketree(r, -1)
checkchild(r)

for _ in range(q):
    x=int(sys.stdin.readline())
    print(num[x]+1)  #본인 포함