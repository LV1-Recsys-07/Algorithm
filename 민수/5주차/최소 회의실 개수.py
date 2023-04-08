import sys
import heapq

n = int(sys.stdin.readline())
time = [] 

for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    time.append((a, b))
    
time.sort(key = lambda x : (x[0], x[1]))

count = 1
temp = [0]

for i in time :
    
    if temp[0] <= i[0] : 
        heapq.heappop(temp)
        
    else : 
        count += 1
        
    heapq.heappush(temp, i[1])
    
print(count)