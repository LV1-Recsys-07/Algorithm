import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [[] * (n + 1) for i in range(n + 1)]

for i in range(n - 1) :
    
    a, b = map(int, sys.stdin.readline().split())
    
    matrix[a].append(b)
    matrix[b].append(a)
    
def bfs(x, matrix) :
    
    queue = deque()
    queue.append(x)
 
    parent = [0] * (n+1)
    
    while queue :
        a = queue.popleft()
        for i in matrix[a] :
            if parent[i] == 0 and i != 1 :
                parent[i] = a
                queue.append(i)
                
    return parent

parent = bfs(1, matrix)

for i in range(2, n + 1) :
    print(parent[i])  