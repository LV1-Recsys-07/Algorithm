import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n, m, r = map(int, input().split())

arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

# min(n, m) / 2 만큼의 사이클이 존재
# 각 사이클의 맨 왼쪽 위 좌표는 (0, 0), (1, 1) ...

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for _ in range(r):
    visited = [[False] * m for _ in range(n)]
    for i in range(min(n, m) // 2):
        r, c = i, i
        k = 0   # 방향
        cur = arr[r][c]
        while True:
            if r == i and c == i + 1:
                arr[i][i] = cur
                break

            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                visited[nr][nc] = True
                nxt = arr[nr][nc]
                arr[nr][nc] = cur
                cur = nxt
                r = nr
                c = nc
            else:
                k = (k + 1) % 4



for row in arr:
    print(*row)

