import sys

n, m = map(int, sys.stdin.readline().split())
cost = [list(map(int, sys.stdin.readline().split())) for i in range(m)] 

dp = [float('inf')] * (n + 100)
dp[0] = 0

for i, j in cost :
    for k in range(j, n + 100) :
        dp[k] = min(dp[k], dp[k - j] + i)
        
print(min(dp[n: ]))