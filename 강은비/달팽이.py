import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
board=[[0 for _ in range(n)] for _ in range(n)]
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

x, y = n//2, n//2
pos=(x+1, y+1)
num=1
board[x][y]=num
times=2
i=0

for step in range(1, n):
    if step==n-1:
        times+=1
    for j in range(times):
        for _ in range(step):
            num+=1
            nx=x+dx[i%4]
            ny=y+dy[i%4]
            board[nx][ny]=num
            if num==k:
                pos=(nx+1, ny+1)
            x, y = nx, ny
        i+=1
            
for s in board:
    print(*s)
print(*pos)

