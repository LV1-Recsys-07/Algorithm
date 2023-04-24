import sys
from collections import defaultdict, deque

edges=defaultdict(list)
n=int(sys.stdin.readline())
for _ in range(n-1):
    x, y=map(int, sys.stdin.readline().split())
    edges[x].append(y)
    edges[y].append(x)

q=deque([(1, 0)])
visit=[0 for _ in range(n+1)]
visit[1]=1
totald=0  #게임을 할 수 있는 횟수는 각 leaf까지의 depth의 합과 같음. 게임이 짝수번에 끝나면 성원이가 진다

while q:                
    x, d=q.popleft()
    leaf=0
    for v in edges[x]:
        if not visit[v]:
            leaf=1
            q.append((v, d+1))
            visit[v]=1
    if not leaf:     #leaf 도달
        totald+=d

if totald%2:     #각 leaf까지의 총 depth의 합이 홀수이면 이김
    print("Yes")
else:
    print("No")
