import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]
visited = [[0] * n for i in range(n)]

# queue를 이용한 bfs
def bfs(x, y, matrix, visited, n) :
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue = deque()
    count = 1
    
    visited[x][y] = 1
    queue.append((x,y))
    
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            # 4방향으로 탐색 진행
            if 0 <= newx < n  and  0 <= newy < n  and visited[newx][newy] == 0 :
                visited[newx][newy] = 1
                if matrix[newx][newy] == 1 :  # 1인 지점을 모두 0으로 바꿈
                    matrix[newx][newy] = 0 
                    queue.append((newx, newy))
                    count += 1
                    
    return count

result = []

# matrix를 돌며 bfs 수행할 때 마다 result에 append
for i in range(n) :
    for j in range(n) :
        if matrix[i][j] == 1 :
            result.append(bfs(i, j, matrix, visited, n))
            
result.sort()

print(len(result))
for i in result :
    print(i)   
