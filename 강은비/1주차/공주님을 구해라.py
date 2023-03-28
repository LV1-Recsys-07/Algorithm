import sys
from collections import deque

def bfs(x, y):
    q=deque([(x, y, 0)]); visit[0][x][y]=1
    while q:
        x, y, flag=q.popleft()
        if x==n-1 and y==m-1 and visit[flag][x][y]-1<=t:
            return visit[flag][x][y]-1
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if flag and not visit[1][nx][ny]:
                    visit[1][nx][ny]=visit[1][x][y]+1
                    q.append((nx, ny, 1))
                elif not flag and board[nx][ny]!=1 and not visit[0][nx][ny]:
                    if board[nx][ny]==2:
                        visit[1][nx][ny]=visit[0][x][y]+1
                        q.append((nx, ny, 1))
                    else:
                        visit[0][nx][ny]=visit[0][x][y]+1
                        q.append((nx, ny, flag))
             
n, m, t=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
dx=[-1, 1, 0, 0]; dy=[0, 0, -1, 1]

answer=bfs(0, 0)
if answer:
    print(answer)
else:
    print("Fail")
