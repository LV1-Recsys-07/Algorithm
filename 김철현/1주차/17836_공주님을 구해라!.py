import sys, math
sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline


def solve():
    global s_time, t
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True
    while q:
        r, c, time = q.popleft()
        if arr[r][c] == 2:                                  # 검을 찾은 경우
            s_time = time + abs(r - n + 1) + abs(c - m + 1) # 검을 가지고 갈 수 있는 최소 시간
        if r == n - 1 and c == m - 1:               # 벽을 안부수고 도착 했을 경우
            return time if time <= t else False     # 최소 시간내에 들어 왔다면 시간을 리턴

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if not visited[nr][nc] and arr[nr][nc] != 1:
                visited[nr][nc] = True
                q.append((nr, nc, time + 1))

    return False

n, m, t = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]
s_time = 10001  # 검을 얻었을 때의 시간
time = solve()
if time:
    print(min(time, s_time))
else:
    if s_time <= t:
        print(s_time)
    else:
        print("Fail")