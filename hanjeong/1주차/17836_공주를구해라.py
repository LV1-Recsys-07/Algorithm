from collections import deque
N, M, T = map(int, input().split())

castle = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs():
    time = float('inf')

    visited[0][0] = 1
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        if castle[x][y] == 2:
            time = N-x-1 + M-y-1 + visited[x][y] -1
        if x == N-1 and y == M-1:
            return min(visited[x][y] - 1, time)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and castle[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return time

answer = bfs()

if answer <= T:
    print(answer)
else:
    print("Fail")
