import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

# matrix 2개 생성
matrix1 = [[] for i in range(n + 1)]
matrix2 = [[] for i in range(n + 1)]

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    
    matrix1[a].append(b)
    matrix1[b].append(a)

    matrix2[a].append(b)
    matrix2[b].append(a)

for i in range(n + 1) :
    
    # 정점 번호가 작은 것 부터 방문하기 위해 정렬
    matrix1[i].sort(reverse = True) 
    matrix2[i].sort()
    
# stack을 이용한 dfs 구현    
def dfs(x, matrix, visited) :
    
    stack = []
    stack.append(x)
      
    while stack :
        a = stack.pop()
        if a not in visited  :   
            visited.append(a) 
            for v in matrix[a] :
                stack.append(v)
                            
    return visited

# queue를 이용한 bfs 구현
def bfs(x, matrix, visited) :
    
    queue = deque()
    
    queue.append(x)
    visited.append(x)
    
    while queue :
        a = queue.popleft()
        for v in matrix[a] :
            if v not in visited :
                visited.append(v)
                queue.append(v) 
                             
    return visited 

visited1 = []
visited2 = []

print(*dfs(v, matrix1, visited1))        
print(*bfs(v, matrix2, visited2))
