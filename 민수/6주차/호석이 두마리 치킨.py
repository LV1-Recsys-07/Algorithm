import sys 

n, m = map(int, sys.stdin.readline().split())
matrix = [[float('inf')] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = 0

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
            
result = float('inf')
answer = []
            
for i in range(n - 1) :
    for j in range(i + 1, n) :
        temp = 0 
        for k in range(n) :
            temp += min(matrix[k][i], matrix[k][j])
            
        if result > temp * 2 :
            result = 2 * temp
            answer = [i + 1, j + 1, 2 * temp]

print(*answer)