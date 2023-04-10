import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

cur = 0
min_cost = int(1e9) + 1
answer = 0
while cur <= n - 2:
    if min_cost > cost[cur]:
        min_cost = cost[cur]
        answer += min_cost * distance[cur]
    else:
        answer += min_cost * distance[cur]
    cur += 1

print(answer)