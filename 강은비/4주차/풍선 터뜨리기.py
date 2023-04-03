import sys
from collections import deque

n=int(sys.stdin.readline())
nums=deque()

for i, v in enumerate(sys.stdin.readline().split()):
    nums.append((i+1, int(v)))

while nums:
    i, x=nums.popleft()
    print(i, end=" ")
    if x>0:
        nums.rotate(1-x)
    else:
        nums.rotate(-x)

    
