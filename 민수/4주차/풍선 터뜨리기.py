import sys
from collections import deque

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

queue = deque((i + 1, n) for i, n in enumerate(number))
result = []

for i in range(n) :
    
    temp = queue.popleft()
    result.append(temp[0])

    if temp[1] >= 0 :
        queue.rotate(-(temp[1] - 1))

    else :
        queue.rotate(-temp[1])

print(*result) 