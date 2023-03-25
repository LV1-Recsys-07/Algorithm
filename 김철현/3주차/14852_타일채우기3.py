import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
p = 10 ** 9 + 7
dp = [0] * (10 ** 6)
dp[0] = 1
dp[1] = 2
k = sum(dp[:2])
for i in range(2, n + 1):
    dp[i] = (2 * k + dp[i - 2]) % p
    k = (k + dp[i]) % p

print(dp[n])
