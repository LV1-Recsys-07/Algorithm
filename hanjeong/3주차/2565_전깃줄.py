# 그 최대연속수열이랑 같아보임
N = int(input())

line = []
for _ in range(N):
    line.append(list(map(int, input().split())))
    
line.sort()
dp = [1 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, i):
        if line[j-1][1] < line[i-1][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))
