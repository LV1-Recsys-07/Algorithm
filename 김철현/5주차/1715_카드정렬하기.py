import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())

arr = []

for i in range(n):
    heapq.heappush(arr, int(input()))

answer = 0

while len(arr) > 1:
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    z = x + y
    answer += z
    heapq.heappush(arr, z)

print(answer)