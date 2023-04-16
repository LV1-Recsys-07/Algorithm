import sys


n, m = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
visited = [[0] * m for i in range(n)]
max_val = 0

def dfs(x, y, matrix, ans, count) :
    
    global max_val
    
    if count == 4 :
        max_val = max(max_val, ans)
        return
        
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    for i in range(4) :
        newx = x + row[i]
        newy = y + col[i]
        
        if 0 <= newx < n and 0 <= newy < m and visited[newx][newy] == 0 :
            visited[newx][newy] = 1
            dfs(newx, newy, matrix, ans + matrix[newx][newy], count + 1)
            visited[newx][newy] = 0
            
            
def new(x, y, matrix) :
    
    global max_val
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    for i in range(4) :
        first = matrix[x][y]
        for j in range(3) :
            a = (i + j) % 4
            newx = x + row[a]
            newy = y + col[a]
            
            if not (0 <= newx < n and 0 <= newy < m) :
                first = 0
                break
                
            first += matrix[newx][newy]
            
        max_val = max(max_val, first)
        
        
for i in range(n) :
    for j in range(m) :
        
        visited[i][j] = 1
        dfs(i, j, matrix, matrix[i][j], 1)
        visited[i][j] = 0
        
        new(i, j, matrix)
        
print(max_val)