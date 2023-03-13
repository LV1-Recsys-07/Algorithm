import sys
sys.stdin = open("input.txt")
from collections import deque


def solve(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1 # 연결된 집의 수
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if graph[nr][nc] == 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
                cnt += 1
    return cnt

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1 and not visited[r][c]:
            result.append(solve(r, c))

print(len(result))
for num in sorted(result):
    print(num)