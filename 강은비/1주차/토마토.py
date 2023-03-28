import sys
from collections import deque

def bfs(ripe):
    dir={0:(-1, 0, 0), 1:(1, 0, 0), 2:(0, -1, 0), 3:(0, 1, 0), 4:(0, 0, -1), 5:(0, 0, 1)}
    day=0; total=0
    q=ripe
    while q:
        q=deque()
        while ripe:
            k, x, y=ripe.popleft()
            total+=1
            for i in range(6):
                nk, nx, ny=dir[i]
                nk+=k; nx+=x; ny+=y
                if 0<=nk<h and 0<=nx<n and 0<=ny<m and board[nk][nx][ny]==0 and not visit[nk][nx][ny]:
                    visit[nk][nx][ny]=1
                    board[nk][nx][ny]=1
                    q.append((nk, nx, ny))
        if q:
            ripe=q
            day+=1
    return day, total

m, n, h=map(int, sys.stdin.readline().split())
board=[[] for _ in range(h)]
visit=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        board[i].append(list(map(int, sys.stdin.readline().split())))

cnt=0; ripe=deque()
for k in range(h):
    for x in range(n):
        for y in range(m):
            if board[k][x][y]==1:
                ripe.append((k, x, y))
            if board[k][x][y]==-1:
                cnt+=1
                
d, t=bfs(ripe)
if t==h*n*m-cnt:
    print(d)
else:
    print(-1)
