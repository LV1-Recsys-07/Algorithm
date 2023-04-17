import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
chicken = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

result = 0 

for i, j, k in combinations(range(m), 3): 
    temp = 0 
    for l in range(n) : 
        temp += max(chicken[l][i], chicken[l][j], chicken[l][k])
        
    if temp > result : 
        result = temp
        
print(result)