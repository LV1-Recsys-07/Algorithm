import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque


n = int(input())    # 보드 크기
K = int(input())    # 사과 개수
apple = [list(map(int, input().rstrip().split())) for _ in range(K)]

L = int(input())    # 방향 변환 정보
direction = deque()
for _ in range(L):
    a, b = input().rstrip().split()
    direction.append((int(a), b))

arr = [[0] * n for _ in range(n)]
for x, y in apple:
    arr[x - 1][y - 1] = 2

q = deque()
q.append((0, 0))
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
idx = 1
cnt = 0
arr[0][0] = 1

while q:
    r, c = q[-1][0], q[-1][1]
    nr, nc = r + dr[idx], c + dc[idx]
    cnt += 1
    if 0 <= nr < n and 0 <= nc < n:
        if arr[nr][nc] == 1:    # 자기 몸과 만나는 경우
            print(cnt)
            exit()
        q.append((nr, nc))
        if arr[nr][nc] == 2:    # 사과 먹은 경우
            arr[nr][nc] = 1
        elif arr[nr][nc] == 0:  # 빈 곳이라면
            arr[nr][nc] = 1
            a, b = q.popleft()  # 꼬리 자르기
            arr[a][b] = 0
    else:                       # 벽인 경우
        print(cnt)
        exit()

    if direction:
        if cnt == direction[0][0]:
            if direction[0][1] == "D":
                idx = (idx + 1) % 4
            else:
                idx = (idx - 1) % 4
            direction.popleft()


