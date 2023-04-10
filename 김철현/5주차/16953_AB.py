import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, 0))


    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt + 1

        for nx in [x * 2, 10 * x + 1]:
            if nx <= int(1e9):
                q.append((nx, cnt + 1))
    return -1

a, b = map(int, input().split())
print(bfs(a, b))
