import sys
from collections import defaultdict, deque


def bfs(q, cnt):
    while q:
        if all(visit):
            return cnt
        x=q.popleft()        
        for y in path[x]:
            if not visit[y]:
                visit[y]=1
                q.append(y)
                cnt+=1

t=int(sys.stdin.readline())
for _ in range(t):
    n, m=map(int, sys.stdin.readline().split())
    path=defaultdict(list)
    visit=[0 for _ in range(n)]
    for _ in range(m):
        a, b=map(int, sys.stdin.readline().split())
        path[a-1].append(b-1)
        path[b-1].append(a-1)
    visit[0]=1
    print(bfs(deque([0]), 0))
    
        