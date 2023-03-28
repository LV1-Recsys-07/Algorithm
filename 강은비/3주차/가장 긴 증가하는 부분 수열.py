import sys

n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))

dp=[1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[j]<a[i] and dp[j]>=dp[i]:  #i가 더 크면서 j도 수열에 포함되어있을 경우만, j에서 끊긴 경우는 제외 
            dp[i]+=1

print(max(dp))
