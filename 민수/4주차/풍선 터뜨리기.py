import sys
from collections import deque

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

queue = deque((i + 1, n) for i, n in enumerate(number)) # 몇 번째 풍선인지도 같이 넣어주기
result = []

for i in range(n) :
    
    temp = queue.popleft() # 1번 풍선 터트리기
    result.append(temp[0])

    if temp[1] >= 0 : # 0보다 크다면 왼쪽으로 queue 회전
        queue.rotate(-(temp[1] - 1)) # popleft 하였으므로 자동으로 1만큼 이동했기 때문에 -1 한 만큼 이동

    else :
        queue.rotate(-temp[1]) # 오른쪽으로 queue 회전

print(*result) 
