import sys

n = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split()))
station = list(map(int, sys.stdin.readline().split()))

cost = station[0]

result = cost * distance[0]

for i in range(n - 2) :
    
    if station[i + 1] < cost : 
        cost = station[i + 1]
        
    result += cost * distance[i + 1]
    
print(result)