import sys
from collections import deque

n, k=map(int, sys.stdin.readline().split())
num=sys.stdin.readline().strip()
digit=deque()

for i in range(n):
    if not digit:
        digit.append(int(num[i]))
    else:
        while n-k-len(digit)<=n-i-1 and digit and digit[-1]<int(num[i]): #기존 마지막 digit보다 클 때 
            digit.pop()                                                  #더 채워야하는 digit 수보다 남은 개수가 많을 때만 pop
        if len(digit)<n-k:
            digit.append(int(num[i]))
print("".join(list(map(str, digit))))