import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]  # 북, 동, 남, 서 방향
dc = [0, 1, 0, -1]

cnt = 0
flag = True

while flag:
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1

    for _ in range(4):  # 4방향 체크
        if d == 0:
            d = 3
        else:
            d -= 1
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            r, c = nr, nc
            break
    else:
        nr = r + dr[(d + 2) % 4]
        nc = c + dc[(d + 2) % 4]
        if arr[nr][nc] == 2:
            r, c = nr, nc
        else:
            flag = False
print(cnt)