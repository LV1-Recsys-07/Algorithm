import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def dfs(x, y, d) :
    
    stack = deque()
    
    stack.append((x, y, d)) # 초기 위치와 방향을 stack에 넣기
    count = 0
    
    row = [0, -1, 0, 1]
    col = [-1, 0, 1, 0]
    
    b_row = [1, 0, -1, 0]
    b_col = [0, -1, 0, 1]
    
    while stack :
        a, b, c = stack.pop()
        
        if graph[a][b] == 0 : # 청소되지 않았다면 청소 실시
            graph[a][b] = -1
            count += 1

        # 후진 방향 설정    
                      
        b_x = a + b_row[c] 
        b_y = b + b_col[c]
        
        # 현재 상태 기록

        flag = 0
        k = c 
        
        for i in range(4) :         
            if graph[a + row[k]][b + col[k]] == 0 :  # 4가지 방향 탐색
                flag = 1
                break 
                
            k = (k - 1) % 4 
            
        # 새로 움직일 방향 설정

        newx = a + row[k]
        newy = b + col[k]
        
        if 0 <= newx < n and 0 <= newy < m :
            if flag == 0 :
                if graph[b_x][b_y] == 1 :  # 벽으로 후진할 경우 작동을 멈춘다
                    break
                    
                else :
                    stack.append((b_x, b_y, c)) # 아닐 경우 처음으로 돌아간다
                    
            else :         
                if graph[newx][newy] == 0 :  # 새로운 방향으로 이동 후 90도 회전
                    new_d = (k - 1) % 4
                    stack.append((newx, newy, new_d))
                      
    return count


result = dfs(r, c, d)   

print(result)