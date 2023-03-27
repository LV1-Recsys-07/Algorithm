import sys

n = int(sys.stdin.readline())

lines = []
for i in range(n) :
    lines.append(list(map(int, sys.stdin.readline().split())))
    
lines.sort(key = lambda x : x[0])

temp = []
for i in range(n) :
    temp.append(lines[i][1])
    
dp = [1] * n

for i in range(n) :
    for j in range(i) :
        if temp[i] > temp[j] :
            dp[i] = max(dp[i], dp[j] + 1)
      
print(n - max(dp))