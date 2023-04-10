import sys
from collections import deque

n = int(sys.stdin.readline())

number = deque(i for i in range(1, n + 1)) # 1번 부터 queue 생성

round = 1

for i in range(n - 1) : # 게임은 n - 1번 진행
    
    target = (round**3) % len(number) # t**3 을 number 길이만큼 나눈 값의 나머지
    
    if target == 1 : # 1이면 맨 앞의 값 pop
        number.popleft()
        
    else : 
        number.rotate(-(target - 1)) # 1보다 크다면 rotate 필요
        number.popleft()
        
    round += 1    
    
print(number[0])
