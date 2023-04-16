import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    j = 1
    while j ** 2 <= i:
        if dp[i] > dp[i - j ** 2] + 1:
            dp[i] = dp[i - j ** 2] + 1
        j += 1

print(dp[n])