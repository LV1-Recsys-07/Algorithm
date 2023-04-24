import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node, depth):
    global cnt
    visited[node] = True
    check = True
    for nxt in graph[node]:
        if not visited[nxt]:
            check = False
            dfs(nxt, depth + 1)
    if check:
        cnt += depth
    return


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
cnt = 0
dfs(1, 0)

if cnt % 2:
    print("Yes")
else:
    print("No")