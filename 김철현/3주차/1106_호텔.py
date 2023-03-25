import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


c, n = map(int, input().split())
# arr[i][0]: 비용 arr[i][1]: 고객 수
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
# dp[i]: i명 늘리는데 필요한 최소 비용
dp = [100000 for _ in range(c + 1)]
dp[0] = 0

for i in range(n):
    for j in range(1, c + 1):
        rest = j - arr[i][1]
        if rest < 0:
            rest = 0
        dp[j] = min(dp[j], dp[rest] + arr[i][0])

print(dp[c])