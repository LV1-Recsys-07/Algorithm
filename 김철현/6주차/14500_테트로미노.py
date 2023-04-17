import sys
sys.stdin = open("input.txt")

'''
1x4: 2가지
2x2: 1가지
니은모양: 8가지
지그재그모양: 4가지
산모양: 4가지
꾸엥
'''

# 긴 막대기 모양 두 종류
def solve1(r, c):
    if c + 3 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r][c+3]
def solve2(r, c):
    if r + 3 >= n:
        return 0
    return arr[r][c] + arr[r+1][c] + arr[r+2][c] + arr[r+3][c]
# 정사각형 모양
def solve3(r, c):
    if r + 1 >= n or c + 1 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r+1][c] + arr[r+1][c+1]
# 니은 모양 8개
def solve4(r, c):
    if r + 2 >= n or c + 1 >= m:
        return 0
    return arr[r][c] + arr[r+1][c] + arr[r+2][c] + arr[r+2][c+1]
def solve5(r, c):
    if r - 1 < 0 or c + 2 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r-1][c+2]
def solve6(r, c):
    if r + 2 >= n or c + 1 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r+1][c+1] + arr[r+2][c+1]
def solve7(r, c):
    if r + 1 >= n or c + 2 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c]
def solve8(r, c):
    if r + 1 >= n or c + 2 >= m:
        return 0
    return arr[r][c] + arr[r+1][c] + arr[r+1][c+1] + arr[r+1][c+2]
def solve9(r, c):
    if r + 2 >= n or c + 1 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r+1][c] + arr[r+2][c]
def solve10(r, c):
    if r - 2 < 0 or c + 1 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r-1][c+1] + arr[r-2][c+1]
def solve11(r, c):
    if r + 1 >= n or c + 2 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+2]
# 지그재그 모양
def solve12(r, c):
    if r + 2 >= n or c + 1 >= m:
        return 0
    return arr[r][c] + arr[r+1][c] + arr[r+1][c+1] + arr[r+2][c+1]
def solve13(r, c):
    if r + 2 >= n or c - 1 < 0:
        return 0
    return arr[r][c] + arr[r+1][c] + arr[r+1][c-1] + arr[r+2][c-1]
def solve14(r, c):
    if r - 1 < 0 or c + 2 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r-1][c+1] + arr[r-1][c+2]
def solve15(r, c):
    if r + 1 >= n or c + 2 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r+1][c+1] + arr[r+1][c+2]
# 산모양
def solve16(r, c):
    if r + 1 >= n or c + 2 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1]
def solve17(r, c):
    if r + 2 >= n or c + 1 >= m:
        return 0
    return arr[r][c] + arr[r+1][c] + arr[r+2][c] + arr[r+1][c+1]
def solve18(r, c):
    if r - 1 < 0 or c + 2 >= m:
        return 0
    return arr[r][c] + arr[r][c+1] + arr[r-1][c+1] + arr[r][c+2]
def solve19(r, c):
    if r + 2 >= n or c - 1 < 0:
        return 0
    return arr[r][c] + arr[r+1][c] + arr[r+1][c-1] + arr[r+2][c]
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
max_sum = 0
for i in range(n):
    for j in range(m):
        max_sum = max(max_sum, solve1(i, j), solve2(i, j), solve3(i, j), solve4(i, j), solve5(i, j),
                      solve6(i, j), solve7(i, j), solve8(i, j), solve9(i, j), solve10(i, j), solve11(i, j),
                      solve12(i, j), solve13(i, j), solve14(i, j), solve15(i, j), solve16(i, j), solve17(i, j),
                      solve18(i, j), solve19(i, j))

print(max_sum)