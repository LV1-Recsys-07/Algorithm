import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dp[node] += 1
            dfs(nxt)
            dp[node] += dp[nxt]
    return


n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0] * (n + 1)
visited = [False] * (n + 1)

dfs(r)
for _ in range(q):
    x = int(input())
    print(dp[x] + 1)