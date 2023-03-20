import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

# 3차원 배열 생성
matrix = [[list(map(int, sys.stdin.readline().split())) for j in range(n)] for i in range(h)]
visited = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]

# queue를 이용한 bfs
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

            if 0 <= newx < n and 0 <= newy < m and 0 <= newz < h and matrix[newz][newx][newy] == 0 : # 0인 지점 찾기  
                queue.append((newx, newy, newz))
                matrix[newz][newx][newy] = matrix[c][a][b] + 1 # 인접한 값 + 1
                
ans = deque()

# 익은 토마토(1)인 지점 찾기
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
            if matrix[i][j][k] == 0 : # bfs를 수행하고 난 후에 0인 지점이 존재하면 -1 print
                print(-1)
                sys.exit(0)
         
            res = max(res, matrix[i][j][k]) # matrix를 탐색하며 가장 큰 값 찾기

print(res - 1)   # 모두 익을 때 까지의 날 이므로 1을 빼고 print
