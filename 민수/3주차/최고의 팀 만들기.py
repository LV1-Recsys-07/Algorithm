import sys

dp = [[0] * 16 for i in range(16)]

while True :
    try :
        white, black = map(int, sys.stdin.readline().split())
        
        for i in reversed(range(16)) :
            for j in reversed(range(16)) :
                if i != 0 :
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + white)
                    
                if j != 0 :
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + black)
                    
    except :
        print(dp[15][15])
        break