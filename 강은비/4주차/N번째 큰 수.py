import sys
import heapq

n=int(sys.stdin.readline())
h=[]
for _ in range(n):
    for x in map(int, sys.stdin.readline().split()):   #input 받아서 바로 처리
        if not h or x>h[0]:
            heapq.heappush(h, x)
        if len(h)>n:
            heapq.heappop(h)

print(heapq.heappop(h))