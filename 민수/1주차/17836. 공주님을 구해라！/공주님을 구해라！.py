import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def bfs(x, y, tx, ty) :
    
    queue = deque()
    visited = [[0] * m for i in range(n)]
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue.append((x, y, 0))
    visited[x][y] = 1
    
    while queue :
        a, b, c = queue.popleft()
        for i in range(4):
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < m and graph[newx][newy] != 1 and visited[newx][newy] == 0 :
                if newx == tx and newy == ty :
                    return c + 1
                
                visited[newx][newy] = 1
                queue.append((newx, newy, c + 1))
                
    return float('inf')

tx, ty = 0, 0

for i in range(n) :
    for j in range(m) : 
        if graph[i][j] == 2 :
            tx, ty = i, j
            
result1 = bfs(0, 0, n - 1, m - 1)

temp = bfs(0, 0, tx, ty)

if temp != float('inf'):
    result2 = temp + abs(n - 1 - tx) + abs(m - 1 - ty)
else:
    result2 = temp

result = min(result1, result2)

if result <= t :
    print(result)
    
else :
    print('Fail')