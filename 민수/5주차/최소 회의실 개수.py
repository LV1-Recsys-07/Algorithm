import sys
import heapq

n = int(sys.stdin.readline())
time = [] 

for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    time.append((a, b))
    
time.sort(key = lambda x : (x[0], x[1])) # 시작시간, 종료시간으로 정렬

count = 1  # 회의실은 최소 1개 이상 필요
temp = [0] # 끝나는 시간 저장할 heap 생성

for i in time :
    
    if temp[0] <= i[0] : # 새로운 회의실이 필요 x
        heapq.heappop(temp)
        
    else : # 새로운 회의실 필요
        count += 1
        
    heapq.heappush(temp, i[1]) # 종료 시간 heap에 넣기
    
print(count)
