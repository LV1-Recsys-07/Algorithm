from collections import deque
n, m, v = map(int, input().split())     #정점, 간선, 시작정점번호
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, result):
    visited[x] = 1
    result.append(x)
    for node in graph[x]:
        if not visited[node]:
            dfs(node, result)

    return result

def bfs(x):
    result = [x]
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        node = queue.popleft()
        for post in graph[node]:
            if not visited[post]:
                visited[post] = 1
                queue.append(post)
                result.append(post)
    return result

#정점의 번호가 작은것부터 방문하므로 정렬해주기
for i in range(1,n+1):
    graph[i].sort()
    
visited = [0]*(n+1)
print(*dfs(v, []))
visited = [0]*(n+1)
print(*bfs(v))