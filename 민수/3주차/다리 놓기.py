import sys
import math

t = int(sys.stdin.readline())

for i in range(t) :
    
    n, m = map(int, sys.stdin.readline().split())
    
    result = math.comb(m, n)
    print(result)