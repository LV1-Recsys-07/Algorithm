import sys

h, w = map(int, sys.stdin.readline().split())

wall = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(1, w - 1) :
    
    # 왼쪽 오른쪽 기둥 높이 계산

    left = max(wall[ :i])
    right = max(wall[i+1: ])
    
    m = min(left, right)

    # 둘중 작은 값이 현재 위치보다 높을 경우 빗물이 고임
    
    if m > wall[i] :
        result += m - wall[i]
        
print(result)