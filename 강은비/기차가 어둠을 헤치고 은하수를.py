import sys
from collections import deque

n, m=map(int, sys.stdin.readline().split())
trains=[deque(["0" for _ in range(20)]) for _ in range(n)]

for _ in range(m):  #m번 명령
    k, i, *x=map(int, sys.stdin.readline().split())
    if k==1:
        if trains[i-1][x[0]-1] == "0":
            trains[i-1][x[0]-1] = "1"
    elif k==2:
        if trains[i-1][x[0]-1] == "1":
            trains[i-1][x[0]-1] = "0"
    elif k==3:
        if trains[i-1][-1] == "1":
            trains[i-1][-1] = "0"
        trains[i-1].rotate(1)
    else:
        if trains[i-1][0] == "1":
            trains[i-1][0] = "0"
        trains[i-1].rotate(-1)

answer=set()   #중복 제외
for t in trains:
    answer.add("".join(t))
print(len(answer))
