C, N = map(int, input().split())

dp = [float('INF') for _ in range(C+101)]
pc_list = [list(map(int, input().split())) for _ in range(N)]
dp[0] = 0
for p, c in pc_list:
    for i in range(c, C+101):
        dp[i] = min(dp[i-c]+p, dp[i])

print(min(dp[C:]))
