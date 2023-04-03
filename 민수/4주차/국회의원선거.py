import sys
import heapq

n = int(sys.stdin.readline())

if n == 1 :
    print(0)
    sys.exit()

target = int(sys.stdin.readline())    
number = []    
    
for i in range(n - 1) :
    heapq.heappush(number, -int(sys.stdin.readline()))
    
count = 0
temp = heapq.heappop(number)

while -temp >= target :
    
    target += 1
    temp += 1
    count += 1
    
    heapq.heappush(number, temp)
    temp = heapq.heappop(number)
    
print(count)