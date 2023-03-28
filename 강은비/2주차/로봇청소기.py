import sys
n, m=map(int, sys.stdin.readline().split())
x, y, d=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dir={0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
visit=[[0 for _ in range(m)] for _ in range(n)]

check=0   #방향 체크
while True:
    visit[x][y]=1
    if check==4:
        if not board[x-1*dir[d][0]][y-1*dir[d][1]]:  #후진
            x=x-1*dir[d][0]
            y=y-1*dir[d][1]
            check=0
        else:
            break
    nx=x+dir[(d+3)%4][0] 
    ny=y+dir[(d+3)%4][1]
    if 0<=nx<n and 0<=ny<m and not board[nx][ny] and not visit[nx][ny]:
        check=0
        x=nx; y=ny
    else:
        check+=1
    d=(d+3)%4   #반시계로 회전
    
print(sum(map(sum, visit)))   #1인 개수

