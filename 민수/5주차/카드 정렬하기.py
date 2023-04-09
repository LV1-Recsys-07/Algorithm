import sys
import heapq

n = int(sys.stdin.readline())
number = []

for i in range(n) :
    heapq.heappush(number, int(sys.stdin.readline()))
    
count, temp = 0, 0

while len(number) > 1 : 
    
    for i in range(2) : 
        temp += heapq.heappop(number)
        
    count += temp 
    heapq.heappush(number, temp)
    temp = 0
    
print(count)