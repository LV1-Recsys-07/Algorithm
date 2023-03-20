import sys

n, m, r = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

rotate = 0

row = [1, 0, -1, 0]
col = [0, 1, 0, -1]

while rotate < r :  # r번 회전
    
    visited = [[0] * m for i in range(n)] # 방문 확인 리스트 
    start_x, start_y = 0, 0 # 시작점 설정
    
    direction = 0 # 움직이는 방향
    x, y = 0, 0
    temp = matrix[x][y]
    
    for i in range(min(n, m) // 2): # 총 반복 횟수
     
        while True :
            newx = x + row[direction]
            newy = y + col[direction]       
            if 0 <= newx < n and 0 <= newy < m and visited[newx][newy] == 0 :  # 조건 만족하고 방문하지 않았다면 숫자 입력
                visited[newx][newy] = 1
                
                new_temp = matrix[newx][newy]
                matrix[newx][newy] = temp
                temp = new_temp
            
                x, y = newx, newy
                             
            else :
                direction = (direction + 1) % 4
            
            if newx == start_x and newy == start_y :  # 원래 지점을 돌아왔으면 (1, 1) 더해준 위치로 이동 후 방향 전환 -> 다시 시작
                x, y = newx + 1, newy + 1
                start_x, start_y = x, y 
                temp = matrix[x][y]
                direction = (direction + 1) % 4
                break    
                
    rotate += 1

for i in matrix :
    print(*i)   
