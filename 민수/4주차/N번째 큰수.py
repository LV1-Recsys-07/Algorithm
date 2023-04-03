import sys
import heapq

n = int(sys.stdin.readline()) 
number = []

for i in range(n) : 
    temp = list(map(int, sys.stdin.readline().split()))
    for j in temp :
        if len(number) < n :
            heapq.heappush(number, j)
            
        elif number[0] < j :
            heapq.heappop(number)
            heapq.heappush(number, j)
            
print(number[0]) 