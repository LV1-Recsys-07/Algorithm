import sys
import itertools

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
        
def find(x) :
    
    global result
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    visited = [[0] * n for i in range(n)]
    
    temp = 0 
    
    for i, j in x :
        visited[i][j] = 1
        temp += matrix[i][j]
        for k in range(4) : 
            newi = i + row[k]
            newj = j + col[k]
            if visited[newi][newj] == 0 :
                visited[newi][newj] = 1
                temp += matrix[newi][newj]
                
            else : 
                return 
            
    result = min(result, temp)
    
    
number = [(i, j) for i in range(1, n - 1) for j in range(1, n - 1)]
result = float('inf')

for i in itertools.combinations(number, 3) :
    find(i)
    
print(result)