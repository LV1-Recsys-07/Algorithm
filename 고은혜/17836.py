from collections import deque
n, m, t = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    result = 1e9
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append((0,0,0))
    while queue:
        x, y, time = queue.popleft()
        if x==n-1 and y==m-1:
            result = min(result, time)
            return result

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if castle[nx][ny]==0:           #빈 칸
                    visited[nx][ny]=1
                    queue.append((nx,ny, time+1))
                elif castle[nx][ny]==1:         #벽
                    continue
                else:                           #그람
                    visited[nx][ny] = 1
                    temp = time+(n-1-nx)+(m-1-ny)+1
                    if temp <= t:
                        result = temp

    return result

result = bfs()
if result <= t:
    print(result)
else:
    print("Fail")