import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs(root):
    q = deque()
    q.append(root)
    visited[root][0] = True

    while q:
        p = q.popleft()

        for c in graph[p]:
            if not visited[c][0]:
                visited[c][0] = True
                q.append(c)
                visited[c][1].append(p)



n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 두번째 배열에는 부모의 노드를 저장
visited = [[False, []] for _ in range(n+1)]
bfs(1)

for i in range(2, n+1):
    print(visited[i][1][0])
