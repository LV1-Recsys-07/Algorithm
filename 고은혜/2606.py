v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    global result
    visited[x] = 1              #중복되면 안 되므로 방문처리
    result += 1
    for node in graph[x]:       #x와 연결된 node 탐색
        if not visited[node]:   #node를 방문하지 않았을 때
            dfs(node)           #깊게 탐색

result = 0
visited = [0]*(v+1)
dfs(1)
print(result-1)