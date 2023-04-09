import sys, heapq
sys.stdin = open("input.txt")

n = int(input())

arr = []

for i in range(n):
    heapq.heappush(arr, int(input()))

answer = 0

while len(arr) > 1:
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)

    answer += x+y
    heapq.heappush(arr, x+y)

print(answer)