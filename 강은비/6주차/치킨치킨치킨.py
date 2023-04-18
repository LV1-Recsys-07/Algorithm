import sys
from itertools import combinations

n, m=map(int, sys.stdin.readline().split())
ratings=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
maxt=-1
for c in combinations(range(m), 3):  #치킨 3가지 선택
    tot=0   #선호도의 합
    for i in range(n):   
        tot+=max([ratings[i][j] for j in c])  #선택한 치킨3 개에 대한 최대 선호도 
    if tot>maxt:
        maxt=tot
print(maxt)
        
