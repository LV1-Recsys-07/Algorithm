import sys
from collections import deque
sys.setrecursionlimit(10**9)

n, r, q = map(int, sys.stdin.readline().split())

matrix = [[] for i in range(n + 1)]  

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)

dp = [0] * (n + 1)    
    
def dfs(x):
    dp[x] = 1
    for i in matrix[x]:
        if not dp[i]:
            dfs(i)
            dp[x] += dp[i]

dfs(r)

for i in range(q) :
    
    temp = int(sys.stdin.readline())
    print(dp[temp])