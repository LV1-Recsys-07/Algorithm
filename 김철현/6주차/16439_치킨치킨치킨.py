import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations as c


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chicken = list(c([i for i in range(m)], 3))
max_value = 0
for a, b, c in chicken:
    temp = 0
    for i in range(n):
        temp += max(arr[i][a], arr[i][b], arr[i][c])
    if max_value < temp:
        max_value = temp

print(max_value)

