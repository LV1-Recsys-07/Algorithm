import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]  # 지도
command = list(map(int, sys.stdin.readline().split()))

dice = [0] * 6  # 주사위 생성

def change(direc) : 
    
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    
    if direc == 1 :  # 동쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
        
    elif direc == 2 :  # 서쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
        
    elif direc == 3 :  # 북쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
        
    else :  # 남쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

# 이동 방향

row = [0, 0, -1, 1]
col = [1, -1, 0, 0]

newx, newy = x, y  # 시작 좌표 설정

for i in command : 
    
    newx += row[i-1]
    newy += col[i-1]
    
    if newx < 0 or newx >= n or newy < 0 or newy >= m : # 지도 밖으로 나갈 경우 해당 명령 무시
        newx -= row[i-1]
        newy -= col[i-1]
        continue 
        
    change(i) # 주사위 이동 수행
    
    if matrix[newx][newy] == 0 :  # 지도에 0이 적혀 있을 때
        matrix[newx][newy] = dice[-1]
        
    else :  # 지도에 0이 적혀 있지 않을 때
        dice[-1] = matrix[newx][newy]  
        matrix[newx][newy] = 0 
        
    print(dice[0]) # 주사위 윗면에 적힌 수 출력