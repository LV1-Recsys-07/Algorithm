import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [[] for i in range(n + 1)]

for i in range(n - 1) :
    a, b = map(int, sys.stdin.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)
    
def find(x) :
    
    queue = deque()
    visited = [0] * (n + 1)
    count = 0 
    
    queue.append(x)
    
    while queue :
        a = queue.popleft()
        
        if len(matrix[a]) == 1 and a != 1 :
            count += visited[a]
            continue
            
        for i in matrix[a] :
            if visited[i] == 0 :
                visited[i] = visited[a] + 1
                queue.append(i)
                
    return count

result = find(1)

if result % 2 == 0 :
    print("No")
    
else : 
    print("Yes")