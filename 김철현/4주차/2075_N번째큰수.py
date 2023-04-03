import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    if not q:                       # 처음 초기 값
        for x in arr:
            heapq.heappush(q, x)
    else:
        for x in arr:               # 가장 큰 5개 값만 있도록 설정
            minimum = heapq.heappop(q)
            if x > minimum:
                heapq.heappush(q, x)
            else:
                heapq.heappush(q, minimum)

print(heapq.heappop(q))

