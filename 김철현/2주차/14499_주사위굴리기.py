import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n, m, r, c, k = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 동 1 서 2 북 3 남 4
cmd = list(map(int, input().rstrip().split()))

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# idx               0   1  2  3  4  5
# 정면에서 봤을 때  아래 위 앞 뒤 왼 오
dice = [0] * 6

for i in range(k):
    direction = cmd[i] - 1
    nr, nc = r + dr[direction], c + dc[direction]
    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        continue
    if direction == 0:  # 동
        a, b, c, d = dice[0], dice[1], dice[4], dice[5]
        dice[0], dice[1], dice[4], dice[5] = d, c, a, b
    elif direction == 1: # 서
        a, b, c, d = dice[0], dice[1], dice[4], dice[5]
        dice[0], dice[1], dice[4], dice[5] = c, d, b, a
    elif direction == 2: # 북
        a, b, c, d = dice[0], dice[1], dice[2], dice[3]
        dice[0], dice[1], dice[2], dice[3] = d, c, a, b
    elif direction == 3: # 남
        a, b, c, d = dice[0], dice[1], dice[2], dice[3]
        dice[0], dice[1], dice[2], dice[3] = c, d, b, a

    if arr[nr][nc]:
        dice[0] = arr[nr][nc]
        arr[nr][nc] = 0
    else:
        arr[nr][nc] = dice[0]

    print(dice[1])

    r = nr
    c = nc



