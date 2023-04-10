import sys
import heapq

n=int(sys.stdin.readline())
h=[]
for _ in range(n):
    for x in map(int, sys.stdin.readline().split()):   #input 받아서 바로 처리
        if not h or x>h[0]:   #현재 top보다 큰 경우 push
            heapq.heappush(h, x)
        if len(h)>n:          #n개 이상 차면 제일 작은 값 pop
            heapq.heappop(h)

print(heapq.heappop(h))       #가장 큰 n개의 수중 가장 작은 값 -> n번째 큰 수