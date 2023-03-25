import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


arr = []
while True:
    try:
        a, b = map(int, input().split())
        arr.append((a, b))
    except:
        break

n = len(arr)
dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(n + 1)]

for i in range(n):
    for w in range(16):
        for b in range(16):
            if w + b > i:
                continue
            if w < 15:  # 백으로 플레이
                dp[i + 1][w + 1][b] = max(dp[i + 1][w + 1][b], dp[i][w][b] + arr[i][0])
            if b < 15:  # 흑으로 플레이
                dp[i + 1][w][b + 1] = max(dp[i + 1][w][b + 1], dp[i][w][b] + arr[i][1])
            # 포함 안시키기
            dp[i + 1][w][b] = max(dp[i + 1][w][b], dp[i][w][b])

print(dp[n][15][15])
