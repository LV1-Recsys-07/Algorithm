import sys
from collections import defaultdict, deque

def findp(parent, x):
    if parent[x]!=x:
        return findp(parent, parent[x])
    return parent[x]

n, m, q=map(int, sys.stdin.readline().split())
water=list(map(int, sys.stdin.readline().split()))
parent=[i for i in range(n)]
tank=defaultdict(list)

for _ in range(m):       #pipe가 있을 때 같은 집합으로 union
    u, v=map(int, sys.stdin.readline().split())
    u=findp(parent, u-1)
    v=findp(parent, v-1)
    if u<v: 
        parent[v]=u  #u를 부모로 
    else:
        parent[u]=v

for i in range(n):       #부모 node 갱신 
    parent[i]=findp(parent, i)
    tank[parent[i]].append(i)

for k in tank:           #각 집합의 고인물 청정물 판별
    new=old=0
    for i in tank[k]:
        if water[i]:
            new+=1
        else:
            old+=1
    if new>old:
        tank[k]=1
    else:
        tank[k]=0

for _ in range(q):
    x=int(sys.stdin.readline())
    print(tank[parent[x-1]])
    

