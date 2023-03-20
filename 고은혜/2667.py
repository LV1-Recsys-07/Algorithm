from collections import deque
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i,j):
    home = 1
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and graph[nx][ny]==1:
                    visited[nx][ny] = 1
                    home += 1
                    q.append((nx,ny))
    return home

count = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]:
            count.append(bfs(i,j))

print(len(count))
count.sort()
for c in count:
    print(c)