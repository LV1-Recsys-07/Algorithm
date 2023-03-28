import sys

c, n=map(int, sys.stdin.readline().split())
l=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]  #cost, num
dp=[float('inf') for _ in range(c+101)] #c 이상에서 최소값이 나올 수 있으므로 
dp[0]=0

for cost, num in l:
    for i in range(1, len(dp)):
        dp[i]=min(dp[i], dp[i-num]+cost)    

print(min(dp[c:]))  #c명을 얻기 위한 최소 비용
