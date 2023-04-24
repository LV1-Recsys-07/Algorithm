import sys
sys.stdin = open("input.txt")
from collections import deque


def bfs(s, e):
    q = deque()
    q.append((s, 0))
    visited[s] = True

    while q:
        node, dist = q.popleft()
        if node == e:
            return dist

        for v in graph[node]:
            if not visited[v[0]]:
                visited[v[0]] = True
                q.append((v[0], dist+v[1]))


# n개의 노드, m개의 출력
n, m = map(int, input().split())


graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


for _ in range(m):
    visited = [False] * (n+1)
    s, e = map(int, sys.stdin.readline().split())
    print(bfs(s, e))

