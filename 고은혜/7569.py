from collections import deque
m, n, h = map(int, input().split())
tomato = deque()
box = [[] for _ in range(h)]

visited = [[[0]*m for _ in range(n)] for _ in range(h)]
for k in range(h):
    for i in range(n):
        b = list(map(int, input().split()))
        box[k].append(b)
        for j in range(m):
            if b[j]==1:
                #tomato가 있는 위치 입력해두기 (z,x,y,day)
                tomato.append((k,i,j,0))
            elif b[j]==-1:
                #미리 방문처리
                #-1이 여러개 모여 둘러쌓여있는 경우에는 가운데에 있는 -1을 확인할 수 없음
                visited[k][i][j]=1

#동, 서, 남, 북, 위, 아래
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,-1,1]

result = 0
while tomato:
    z, x, y, day = tomato.popleft()
    visited[z][x][y] = 1
    for k in range(6):
        nx = x+dx[k]
        ny = y+dy[k]
        nz = z+dz[k]
        if 0<=nx<n and 0<=ny<m and 0<=nz<h and not visited[nz][nx][ny]:
            if box[nz][nx][ny]==0:
                box[nz][nx][ny]=1
                visited[nz][nx][ny]=1
                result = day+1  #result를 day+1가 아닌 +1을 하게 되면 토마토가 익는 만큼 증가하게 됨
                tomato.append((nz,nx,ny,day+1))

flag = True
for k in range(h):
    for i in range(n):
        for j in range(m):
            if not visited[k][i][j]:
                flag = False
                break
        if not flag:
            break

#-1은 미리 방문처리 했으므로
#모두 방문처리 됐다면, 모든 토마토가 익을 수 있는 경우를 뜻함
if flag:
    print(result)
else:
    print(-1)