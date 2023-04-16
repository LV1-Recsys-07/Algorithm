import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
import math
from copy import deepcopy

"""
1 2 3 4 5
2 3 4 5 1
4 5 2 3 1
5 4 2 3 1
"""

def solve(k):
    global temp
    sub = temp[n - 2 ** k:]
    res = temp[:n - 2 ** k]
    for i in range(2, k + 2):
        res = sub[:len(sub) - 2 ** (k - i + 1)] + res
        sub = sub[len(sub) - 2 ** (k - i + 1):]

    temp = sub + res

    return



n = int(input())
target = list(map(int, input().rstrip().split()))
origin = [i for i in range(1, n + 1)]
max_k = int(math.log(n, 2))


for i in range(1, max_k + 1):
    for j in range(1, max_k + 1):
        temp = deepcopy(origin)
        solve(i)
        solve(j)

        if temp == target:
            print(i, j)
            exit()

