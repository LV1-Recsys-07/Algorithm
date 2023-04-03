import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [[0] * n for i in range(n)]
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]

queue = deque()
queue.append((0, 0))

k = int(sys.stdin.readline())

for i in range(k) : 
    x, y = map(int, sys.stdin.readline().split())
    matrix[x - 1][y - 1] = 2
    
l = int(sys.stdin.readline())
direction = {}

for i in range(l) :
    num, d = sys.stdin.readline().split()
    direction[int(num)] = d
        
x, y = 0, 0
matrix[x][y] = 1

count = 0
way = 0

def turn(d):
    global way
    if d == 'L':
        way = (way - 1) % 4
    else:
        way = (way + 1) % 4
        
while True :
    count += 1
    x += row[way]
    y += col[way]
    
    if x < 0 or x >= n or y < 0 or y >= n:
        break
        
    if matrix[x][y] == 2 :
        matrix[x][y] = 1
        queue.append((x, y))
        if count in direction : 
            turn(direction[count])
            
    elif matrix[x][y] == 0 :
        matrix[x][y] = 1
        queue.append((x, y))
        newx, newy = queue.popleft()
        matrix[newx][newy] = 0
        if count in direction :
            turn(direction[count])
            
    else :
        break
        
print(count)