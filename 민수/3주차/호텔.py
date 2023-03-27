import sys

n, m = map(int, sys.stdin.readline().split())
cost = [list(map(int, sys.stdin.readline().split())) for i in range(m)] 

# 얻을 수 있는 고객의 수가 100보다 작거나 같은 자연수

dp = [float('inf')] * (n + 100)
dp[0] = 0

# 늘어나는 고객수에 따른 최소 비용 업데이트

for i, j in cost :
    for k in range(j, n + 100) :
        dp[k] = min(dp[k], dp[k - j] + i)
        
print(min(dp[n: ]))
