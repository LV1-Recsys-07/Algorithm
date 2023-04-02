import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque


n = int(input())
arr = list(map(int, input().rstrip().split()))

q = deque([[i + 1, arr[i]] for i in range(n)])

result = []
while q:
    result.append(q[0][0])
    a, b = q.popleft()
    if b > 0:
        for _ in range(b - 1):
            q.rotate(-1)
    elif b < 0:
        b = -b
        for _ in range(b):
            q.rotate()

print(*result)

