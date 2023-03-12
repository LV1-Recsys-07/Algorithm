N = int(input())

graph = {i: set() for i in range(1, N+1)}
visited = set()
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(v, g):
    if v in visited:
        return
    visited.add(v)
    if v in g:
        for w in g[v]:
            dfs(w, g)
    return

dfs(1, graph)

print(len(visited) - 1)
