import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

def solve():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if nz < 0 or nz >= h or ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            # 토마토가 아닌 경우
            if arr[nz][ny][nx] == -1:
                continue
            # 안익은 토마토인 경우
            if arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                q.append((nz, ny, nx))

# 가로, 세로, 높이
m, n, h = map(int, input().split())
arr = []
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    arr.append(temp)

# 위 아래 상 하 좌 우
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]


q = deque()
flag1 = True # 처음에 익은 토마토만 있을 경우 대비
for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x] == 0:
                flag1 = False
            elif arr[z][y][x] == 1: # 익은애들 먼저 넣어놓기
                q.append((z, y, x))

solve()

cnt = -1
flag2 = False # 안 익은 토마토가 있을 경우 대비
for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x] == 0:
                flag2 = True
            if arr[z][y][x] > cnt:
                cnt = arr[z][y][x]

if flag1:   # 모든 토마토가 익어있는 상태
    print(0)
elif flag2: # 안익은 토마토가 있는 경우
    print(-1)
else:
    print(cnt - 1)