import sys

n = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split())) # 거리
station = list(map(int, sys.stdin.readline().split())) # 리터 당 가격

cost = station[0] # 첫 번째 station은 무조건 지나가야함

result = cost * distance[0] # 두 번째 station 까지 이동

for i in range(n - 2) : # 남은 거리는 n - 2개
    
    if station[i + 1] < cost : # 새로 방문한 station의 가격이 더 낮다면
        cost = station[i + 1]
        
    result += cost * distance[i + 1]
    
print(result)
