N = int(input())

dp = [0, 0, 0, 0]

dp[0], dp[1], dp[2] = 2, 7, 22
for _ in range(4, N+1):
    dp[3] = 2*dp[0] + 3*dp[1] + 2*dp[2] # 메모리초과 때문에 방식 바꿔봄
    for i in range(3):
        dp[i] = dp[i+1]

if N < 3:
    print(dp[N])
else:   
    print(dp[-1] % 1000000007)
