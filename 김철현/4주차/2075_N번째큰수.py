import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    if not q:
        for x in arr:
            heapq.heappush(q, x)
    else:
        for x in arr:
            minimum = heapq.heappop(q)
            if x > minimum:
                heapq.heappush(q, x)
            else:
                heapq.heappush(q, minimum)

print(heapq.heappop(q))

