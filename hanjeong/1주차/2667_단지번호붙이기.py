N = int(input())

map_list = [list(map(int, list(input()))) for _ in range(N)]

num_houses = []

def dfs(i, j):
    global cnt
    if map_list[i][j] == 0:
        return
    map_list[i][j] = 0
    cnt += 1

    if i > 0 and map_list[i-1][j] == 1:
        dfs(i-1,j)
    if i < N-1 and map_list[i+1][j] == 1:
        dfs(i+1, j)
    if j > 0 and map_list[i][j-1] == 1:
        dfs(i, j-1)
    if j < N-1 and map_list[i][j+1] == 1:
        dfs(i, j+1)


for i in range(0, N):
    for j in range(0, N):
        cnt = 0
        dfs(i, j)
        if cnt != 0:
            num_houses.append(cnt)

print(len(num_houses))
for n in sorted(num_houses):
    print(n)
