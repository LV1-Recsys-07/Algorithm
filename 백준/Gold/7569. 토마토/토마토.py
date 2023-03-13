import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

matrix = [[list(map(int, sys.stdin.readline().split())) for j in range(n)] for i in range(h)]
visited = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]

def bfs(queue, matrix, visited, m, n, h) :   
       
    row = [1, -1, 0, 0, 0, 0]
    col = [0, 0, 1, -1, 0, 0]
    hei = [0, 0, 0, 0, 1, -1]
    
    while queue :
        a, b, c = queue.popleft()
    
        for i in range(6) :
            newx = a + row[i]
            newy = b + col[i]
            newz = c + hei[i]

            if 0 <= newx < n and 0 <= newy < m and 0 <= newz < h and matrix[newz][newx][newy] == 0:
                queue.append((newx, newy, newz))
                matrix[newz][newx][newy] = matrix[c][a][b] + 1
                
ans = deque()

for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if matrix[i][j][k] == 1:
                ans.append((j, k, i))
                
bfs(ans, matrix, visited, m, n, h)
res = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0 :
                print(-1)
                sys.exit(0)
         
            res = max(res, matrix[i][j][k])

print(res - 1)


            
    