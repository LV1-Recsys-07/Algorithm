# 시간 초과...
N, M, R = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

num_sqr = min(N, M) // 2

for _ in range(R): # 한 번에 r칸씩 보내는게 낫나?
    for i in range(num_sqr):
        tmp = arr[i][i]
        for j in range(i, M-i-1): # 위
            arr[i][j] = arr[i][j+1]
        for j in range(i, N-i-1): # 오
            arr[j][M-i-1] = arr[j+1][M-i-1]
        for j in range(M-i-1, i, -1): # 아
            arr[N-i-1][j] = arr[N-i-1][j-1]
        for j in range(N-i-1, i, -1): # 왼
            arr[j][i] = arr[j-1][i]
        arr[i+1][i] = tmp


for row in arr:
    for r in row:
        print(r, end=" ")
    print()