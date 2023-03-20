import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

k = n ** 2 # 표 크기

matrix = [[0] * n for i in range(n)]
matrix[0][0] = k # 표 첫 번째 부분에 입력
k -= 1 # k 값 1 감소

row = [1, 0, -1, 0]
col = [0, 1, 0, -1]

a, b = 0, 0
i = 0

# 숫자 입력

while k > 0 :
    
    newx = a + row[i]
    newy = b + col[i]
    
    if newx < 0 or newx >= n or newy < 0 or newy >= n or matrix[newx][newy] != 0 : # 한 방향으로 모두 이동 or 모든 지점 채우면 방향 바꿈
        i = (i + 1) % 4
        continue
        
    matrix[newx][newy] = k
    a, b = newx, newy

    k -= 1
    
x, y = 0, 0

for i in range(len(matrix)) :
    print(*matrix[i])

    if m in matrix[i] :
        x, y = i, matrix[i].index(m)

print(x+1, y+1)           
