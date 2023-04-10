import sys
import heapq

n=int(sys.stdin.readline())
sch=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]  #회의 스케쥴
sch.sort()

rooms=[]
heapq.heappush(rooms, 0)   #회의 끝나는 시간 저장

for s, e in sch:
    if s>=rooms[0]:    #가장 빨리 끝나는 회의실보다 시작 시간이 큰 경우 
        heapq.heappop(rooms)
        heapq.heappush(rooms, e)    #회의 시간 업데이트 
    else:
        heapq.heappush(rooms, e)    #새로운 회의실 추가

print(len(rooms))