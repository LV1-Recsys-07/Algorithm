import sys
from collections import defaultdict, deque

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    pt=dict()
    for _ in range(n-1):
        a, b=map(int, sys.stdin.readline().split())
        pt[b]=a
    x, y=map(int, sys.stdin.readline().split())
    path=set()  #조상으로 가는 경로
    while True:
        path.add(x)
        p=pt.get(x, -1)
        if p==-1:
            break
        x=p
    while True:
        if y in path:
            print(y)
            break
        p=pt.get(y, -1)
        if p==-1:
            break
        y=p

        