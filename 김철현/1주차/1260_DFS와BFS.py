import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque


def dfs(x):
    ls_dfs.append(x)
    visited[x] = True
    for nxt in graph[x]:
        if not visited[nxt]:
            dfs(nxt)
    return


def bfs():
    q = deque()
    q.append(v)
    visited[v] = True
    ls_bfs.append(v)

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                ls_bfs.append(nxt)
                q.append(nxt)
                visited[nxt] = True
    return


n, m, v = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):   # 오름차순 정렬
    graph[i].sort()

ls_dfs = []
ls_bfs = []
visited = [False] * (n + 1)
dfs(v)
visited = [False] * (n + 1)
bfs()
print(*ls_dfs)
print(*ls_bfs)