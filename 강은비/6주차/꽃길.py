import sys
from itertools import combinations

n=int(sys.stdin.readline())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx=[0, -1, 0, 1, 0]
dy=[0, 0, -1, 0, 1]
locs=[(x, y) for x in range(1, n-1) for y in range(1, n-1)]   #좌표 후보
m=10000

for c in combinations(locs, 3):
    total=0
    visit=[[0 for _ in range(n)] for _ in range(n)]
    flag=True
    for x, y in c:
        for i in range(5):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                total+=board[nx][ny]
                visit[nx][ny]=1
            else:           #겹칠 때
                flag=False
                break
        if not flag:
                break
    else:
        if total<m:
            m=total

print(m)