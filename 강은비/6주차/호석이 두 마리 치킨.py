import sys
from collections import defaultdict, deque
from itertools import combinations

n, m=map(int, sys.stdin.readline().split())
dist=[[float('inf') for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y=map(int, sys.stdin.readline().split())   
    dist[x-1][y-1]=1      #바로 연결되는 경우
    dist[y-1][x-1]=1

for i in range(n):
    dist[i][i]=0

for k in range(n):   #거쳐서 가는 경우 
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])   #모든 건물 사이간 거리 갱신
#print(dist)

answer=[]
for c in combinations(range(n), 2):
    ck1, ck2=c    #치킨 집 두개 선택
    t=0
    for i in range(n):
        t+=2*min(dist[i][ck1], dist[i][ck2])   #모든 건물에서 가장 가까운 치킨집까지의 거리 
    answer.append((ck1+1, ck2+1, t))
answer.sort(key=lambda x: (x[2], x[0], x[1]))
print(*answer[0])