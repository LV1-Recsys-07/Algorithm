import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

vertex = [[]* n for i in range(n + 1)]

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    
    vertex[a].append(b)
    vertex[b].append(a) 

# stack을 이용한 dfs로 탐색    
def dfs(start, vertex) : 

    visited = []
    stack = [start]

    while stack :
        v = stack.pop()
        if v not in visited : 
            visited.append(v)
            for w in vertex[v] : # 연결되어 있는 점들만 stack에 들어감
                stack.append(w) 
                
    return visited
            
a = dfs(1, vertex)
print(len(a) - 1)
