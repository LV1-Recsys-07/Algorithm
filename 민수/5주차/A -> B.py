import sys
from collections import deque, defaultdict

a, b = map(int, sys.stdin.readline().split())
visited = defaultdict(int) # 방문 순서 기록

def bfs(x, visited) :
    
    queue = deque()
    
    queue.append(x)
    visited[x] = 0
    
    while queue :
        a = queue.popleft()
        if a == b :
            return visited[a] + 1
        
        for i in (2 * a, 10 * a + 1) : # 2가지 방식으로 이동
            if i <= b and visited[i] == 0 :
                visited[i] = visited[a] + 1
                queue.append(i) 

    return -1
                
print(bfs(a, visited))
