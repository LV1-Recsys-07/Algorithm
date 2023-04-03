import sys
from collections import deque

n=int(sys.stdin.readline())
people=deque([x+1 for x in range(n)])   #각 사람의 번호 
t=1

while people:
    x=people.popleft()        #현재 백준이 앞에 서있는 사람
    t+=1
    people.rotate(1-t**3)     #시계방향으로 이동

print(x)


