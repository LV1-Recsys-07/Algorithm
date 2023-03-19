from collections import deque

M, N, H = map(int, input().split())

box = []
is_tomato = False
for _ in range(H):
    floor = []
    for _ in range(N):
        row  = list(map(int, input().split())) # 여기서 queue에 넣어도 될 것 같긴 한데 귀찮
        if 0 in row:
            is_tomato = True
        floor.append(row)
    box.append(floor)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()

def bfs():
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y]+1
                    q.append((nz,nx,ny))
if not is_tomato:
    print(0)
else:
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    q.append((i,j,k))

    bfs()
    answer = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    print(-1)
                    exit(0)            
                answer = max(answer, box[i][j][k])

    print(answer-1)
