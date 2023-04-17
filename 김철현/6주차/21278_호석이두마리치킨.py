import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for r in range(1, n + 1):
    for c in range(1, n + 1):
        if r == c:
            graph[r][c] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


min_v1 = 0
min_v2 = 0
min_distance = INF * n

for i in range(1, n):
    for j in range(i, n + 1):
        temp = 0
        for k in range(1, n + 1):
            if k != i and k != j:
                temp += min(graph[i][k], graph[j][k])
        if temp < min_distance:
            min_v1 = i
            min_v2 = j
            min_distance = temp

print(min_v1, min_v2, min_distance * 2)
