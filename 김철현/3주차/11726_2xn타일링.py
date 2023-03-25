import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
p = 10007
dp = [0] * 1001
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % p

print(dp[n])
