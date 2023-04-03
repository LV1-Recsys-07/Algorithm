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
        q.rotate(-(b - 1))    # 반시계 방향 회전
    elif b < 0:
        q.rotate(-b)      # 시계방향 회전

print(*result)

