import sys
import heapq

n = int(sys.stdin.readline())
number = []

for i in range(n) :
    heapq.heappush(number, int(sys.stdin.readline())) # heap에 카드 넣기
    
count, temp = 0, 0

while len(number) > 1 : 
    
    for i in range(2) : # 제일 작은 2장 뽑아서 더하기
        temp += heapq.heappop(number)
        
    count += temp 
    heapq.heappush(number, temp) # 다시 heap에 푸시
    temp = 0
    
print(count)
