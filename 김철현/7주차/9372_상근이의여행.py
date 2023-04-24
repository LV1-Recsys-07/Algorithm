import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

def solve(x):
    global answer
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                answer += 1

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    answer = 0
    for i in range(1, n + 1):
        if not visited[i]:
            solve(i)
    print(answer)