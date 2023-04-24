import sys

def dfs(x, y, cnt, s):   #상하좌우 4칸 탐색 -> 테트로미노
    global M
    if cnt==4:
        if s>M:
            M=s
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
            if cnt==2:  #ㅏ, ㅜ, ㅓ, ㅏ
                visit[nx][ny]=1
                dfs(x, y, cnt+1, s+board[nx][ny])   #원래 좌표로 돌아와서 탐색
                visit[nx][ny]=0

            visit[nx][ny]=1
            dfs(nx, ny, cnt+1, s+board[nx][ny])
            visit[nx][ny]=0


n, m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit=[[0 for _ in range(m)] for _ in range(n)]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
M=-1

for i in range(n):
    for j in range(m):
        visit[i][j]=1
        dfs(i, j, 1, board[i][j])   
        visit[i][j]=0

print(M)