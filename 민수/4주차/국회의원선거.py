import sys
import heapq

n = int(sys.stdin.readline())

if n == 1 :  # 1명인 경우 매수할 필요 x
    print(0)
    sys.exit()

target = int(sys.stdin.readline())    
number = []    
    
for i in range(n - 1) : # heap에 내림차순으로 넣어줌
    heapq.heappush(number, -int(sys.stdin.readline()))
    
count = 0
temp = heapq.heappop(number) # 가장 큰 득표수 pop

while -temp >= target : # target보다 크거나 같을 때 while 문 반복
    
    target += 1
    temp += 1
    count += 1 # 투표 조작 횟수
    
    heapq.heappush(number, temp)
    temp = heapq.heappop(number)
    
print(count)
