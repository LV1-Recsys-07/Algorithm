# 시간 초과
# from itertools import combinations
# N = int(input())

# for _ in range(N):
#     a, b = map(int, input().split())
#     print(len(list(combinations([i for i in range(b)], a))))

import math

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    print(math.factorial(b)//(math.factorial(b-a)*math.factorial(a)))

# dp로도 풀어보기
