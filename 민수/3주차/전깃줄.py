import sys

n = int(sys.stdin.readline())

lines = []
for i in range(n) :
    lines.append(list(map(int, sys.stdin.readline().split())))
    
# 첫 번째 값으로 배열 정렬

lines.sort(key = lambda x : x[0])

temp = []

# 두 번째 값으로만 이루어진 배열 생성

for i in range(n) :
    temp.append(lines[i][1])
    
dp = [1] * n

# 가장 긴 증가하는 부분수열 문제로 변화

for i in range(n) :
    for j in range(i) :
        if temp[i] > temp[j] :
            dp[i] = max(dp[i], dp[j] + 1)
      
print(n - max(dp))
