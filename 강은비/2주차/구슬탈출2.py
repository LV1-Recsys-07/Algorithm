import sys
from collections import deque
    
def bfs(rx, ry, bx, by):
    q=deque([(rx, ry, bx, by, 0)])
    visited=set()
    visited.add((rx, ry, bx, by))
    while q:
        rx, ry, bx, by, cnt=q.popleft()
        if cnt>=10:
            return -1
        for i in range(4):
            rcnt, nrx, nry=check(rx, ry, i)
            bcnt, nbx, nby=check(bx, by, i)
            if board[nbx][nby]!="O":     #파란구슬이 구멍에 안들어갔을 때에만
                if board[nrx][nry]=="O":
                    return cnt+1
                if nrx==nbx and nry==nby:
                    if rcnt>bcnt:         #파란 구슬이 더 앞서있던 상황 -> 빨간구슬 뒤로
                        nrx-=dx[i]
                        nry-=dy[i]
                    else:
                        nbx-=dx[i]
                        nby-=dy[i]
            if not set([(nrx, nry, nbx, nby)])&visited:
                q.append((nrx, nry, nbx, nby, cnt+1))
    return -1

def check(x, y, i):
    cnt=0
    while 0<=x+dx[i]<n and 0<=y+dy[i]<m and board[x+dx[i]][y+dy[i]]!="#" and board[x][y]!="O":  # 다음칸이 #이면 현재에서 멈춤, 현재칸이 구멍이면 멈춤
        cnt+=1            
        x+=dx[i]
        y+=dy[i] 
    return (cnt, x, y)    

n, m=map(int, sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]

for i in range(n):
    for j in range(m):
        if board[i][j]=="R":
            rx, ry=i, j
        elif board[i][j]=="B":
            bx, by=i, j

print(bfs(rx, ry, bx, by))
