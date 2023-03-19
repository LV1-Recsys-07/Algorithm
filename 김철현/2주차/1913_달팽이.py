import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
m = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
r = c = 0
num = n ** 2
k = 0
while True:
    arr[r][c] = num
    if r == (n - 1) // 2 and c == (n - 1) // 2:
        break
    nr = r + dr[k]
    nc = c + dc[k]
    if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
        r = nr
        c = nc
    else:
        k = (k + 1) % 4
        r += dr[k]
        c += dc[k]

    num -= 1

for row in arr:
    print(*row)

for i in range(n):
    for j in range(n):
        if arr[i][j] == m:
            print(i + 1, j + 1)
            exit()