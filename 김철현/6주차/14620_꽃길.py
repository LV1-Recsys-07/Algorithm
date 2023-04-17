import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from itertools import combinations


n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

ls = []
# 테두리 빼고 빈 리스트에 넣기
for r in range(1, n - 1):
    for c in range(1, n - 1):
        ls.append((r, c))

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
answer = 3000 # 200 * 5 * 3

# 가능한 지점 중 3개씩 뽑아서 확인
for candidate in combinations(ls, 3):
    visited = []
    check = False
    price = 0
    for r, c in candidate:
        for k in range(5):
            nr, nc = r + dr[k], c + dc[k]
            if (nr, nc) in visited:
                check = True
                break
            else:
                price += arr[nr][nc]
                visited.append((nr, nc))
        if check:
            break
    if not check:
        if price < answer:
            answer = price


print(answer)