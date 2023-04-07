import sys

n=int(sys.stdin.readline())
dist=list(map(int, sys.stdin.readline().split()))
cities=list(map(int, sys.stdin.readline().split()))

cost=0
min_c=float('inf')  #최소 가격

for i in range(len(cities)-1):  #마지막 주유소는 의미x
    if cities[i]<min_c:
        min_c=cities[i]
    cost+=min_c*dist[i]

print(cost)