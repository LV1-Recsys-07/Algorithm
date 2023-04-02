import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
import heapq

n = int(input())
x = int(input())
q = []
for _ in range(n - 1):
    heapq.heappush(q, -int(input()))
cnt = 0
while q:
    other = -heapq.heappop(q)
    if x > other:
        break
    x += 1
    cnt += 1
    other -= 1
    heapq.heappush(q, -other)

print(cnt)


