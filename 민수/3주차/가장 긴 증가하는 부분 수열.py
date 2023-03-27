import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [1] * n # dp 배열 생성

# for문을 돌면서 i가 이전 수보다 크다면 업데이트

for i in range(1, n) :
    for j in range(i) :
        if numbers[i] > numbers[j] :
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))
