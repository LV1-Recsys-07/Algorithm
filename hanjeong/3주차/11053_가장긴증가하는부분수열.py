N = int(input())

arr = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]
dp[1] = 1

for i in range(2, N+1):
    max_dp = 1
    for j in range(1, i):
        if arr[j-1] < arr[i-1]:
            if max_dp < dp[j]:
                max_dp = dp[j]
    dp[i] = max_dp + 1

print(dp)
print(max(dp))