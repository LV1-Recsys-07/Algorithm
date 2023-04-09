import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
import heapq

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

q = []
arr.sort()

for i in range(n):
    start, end = arr[i][0], arr[i][1]
    if not q:
        heapq.heappush(q, (end, start))
    else:
        if start >= q[0][0]:
            heapq.heappop(q)
        heapq.heappush(q, (end, start))


print(len(q))

