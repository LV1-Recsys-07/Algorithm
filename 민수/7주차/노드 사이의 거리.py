import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, l = map(int, sys.stdin.readline().split())
    matrix[a].append((b, l))
    matrix[b].append((a, l))
    
def bfs(x, y) :
    
    queue = deque()
    visited = [0] * (n + 1)
    
    queue.append((x, 0))
    visited[x] = 1
    
    while queue :
        a, b = queue.popleft()
        
        if a == y :
            return b
        
        for i, j in matrix[a] :
            if visited[i] == 0 :
                visited[i] = 1
                queue.append((i, b + j))

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))