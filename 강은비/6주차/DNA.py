import sys
from collections import Counter

n, m=map(int, sys.stdin.readline().split())
d=[[] for _ in range(m)]

answer=""
dist=0
for _ in range(n):
    dna=sys.stdin.readline().strip()
    for i in range(m):     #각 index에 해당하는 dna 문자 저장
        d[i].append(dna[i])

for x in d:
    c=sorted(Counter(x).items(), key=lambda x : (-x[1], x[0]))
    answer+=c[0][0]  #해당 index에서 가장 많이 나온 문자 추가
    for i in range(1, len(c)):
        dist+=c[i][1]  #나머지 문자에 대한 distance 증가

print(answer)
#print(dist)

