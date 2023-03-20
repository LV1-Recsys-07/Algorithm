import sys
from collections import defaultdict

n = int(sys.stdin.readline())

matrix = [[0] * n for i in range(n)]

like = defaultdict(list)

row = [1, -1, 0, 0] 
col = [0, 0, 1, -1]

for i in range(n**2) :
    num = list(map(int, sys.stdin.readline().split()))
    
    like[num[0]] = num[1:]  # 딕셔너리 생성 후 좋아하는 학생 넣기
       
    x = 0
    y = 0
    
    like_count = -1
    empty_count = -1
    
    for i in range(n) :
        for j in range(n) :
            if matrix[i][j] == 0 :
                like_temp = 0
                empty_temp = 0
                for k in range(4) :
                    newx = i + row[k]
                    newy = j + col[k]
                    if 0 <= newx < n and 0 <= newy < n :
                        if matrix[newx][newy] in like[num[0]] :
                            like_temp += 1
                        
                        if matrix[newx][newy] == 0 :
                            empty_temp += 1
                            
                    if like_count < like_temp or (like_count == like_temp and empty_count < empty_temp) : # 좋아하는 학생 수 계산 후 비어있는 칸이 가장 많은 곳 찾기
                        x = i
                        y = j
                        like_count = like_temp
                        empty_count = empty_temp
                        
    matrix[x][y] = num[0]   

result = 0

# 만족도 계산

for i in range(n) :
    for j in range(n) :
        count = 0        
        for k in range(4) :
            newx = i + row[k]
            newy = j + col[k]
            if 0 <= newx < n and 0 <= newy < n :
                if matrix[newx][newy] in like[matrix[i][j]] :
                    count += 1
                    
        if count != 0 :
            result += 10 ** (count - 1)

print(result)            