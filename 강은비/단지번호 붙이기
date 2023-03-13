import sys
from collections import deque

n=int(sys.stdin.readline())
board=[]
for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline().strip('\n')))))
visit=[[0 for _ in range(n)] for _ in range(n)]; answer=[]

def bfs(sx, sy):
    q=deque([(sx, sy)]); visit[sx][sy]=1
    dx=[-1, 0, 1, 0]; dy=[0, 1, 0, -1]
    cnt=1 
    while q:  
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and board[nx][ny]:
                visit[nx][ny]=1
                q.append((nx, ny))
                cnt+=1
    return cnt

for i in range(n):
    for j in range(n):
        if not visit[i][j] and board[i][j]:
            k=bfs(i, j)
            if k>0: answer.append(k)

answer.sort()
print(len(answer))
for x in answer:
    print(x)



