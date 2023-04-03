import sys
from collections import deque

n = int(sys.stdin.readline())

number = deque(i for i in range(1, n + 1))

round = 1

for i in range(n - 1) :
    
    target = (round**3) % len(number)
    
    if target == 1 :
        number.popleft()
        
    else : 
        number.rotate(-(target - 1))
        number.popleft()
        
    round += 1    
    
print(number[0])