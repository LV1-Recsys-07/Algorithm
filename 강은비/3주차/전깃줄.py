import sys

n=int(sys.stdin.readline())
line=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
line.sort()
line=list(map(lambda x: x[1], line))
dp=[1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if line[j]<line[i]:   #i가 더 큰 경우에만 
            dp[i]=max(dp[i], dp[j]+1)  #j에서 끊기는 경우 / j에서 이어지는 경우 +1

print(n-max(dp))