import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)

if n == 1 :
    print(2)
    sys.exit()
    
elif n == 2 :
    print(7)
    sys.exit()

dp[1] = 2
dp[2] = 7
dp[3] = 22

for i in range(4, n + 1) :
    dp[i] = (3 * dp[i-1] + dp[i-2] - dp[i-3]) % 1000000007
    
print(dp[n])