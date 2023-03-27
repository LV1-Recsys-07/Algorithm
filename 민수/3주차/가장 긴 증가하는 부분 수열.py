import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [1] * n 

for i in range(1, n) :
    for j in range(i) :
        if numbers[i] > numbers[j] :
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))