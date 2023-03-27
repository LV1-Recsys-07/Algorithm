import sys

n = int(sys.stdin.readline())

dp = [0] * 1001 # dp 리스트 생성

dp[1] = 1 # 2 x 1 case 
dp[2] = 2 # 2 x 2 case

for i in range(3, n + 1) :
    dp[i] = (dp[i-1] + dp[i-2]) % 10007 # 점화식으로 풀이
    
print(dp[n])
