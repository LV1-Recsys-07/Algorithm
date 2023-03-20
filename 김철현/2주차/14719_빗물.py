import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


h, w = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
rain = [[0] * w for _ in range(h)]

for i in range(w):
    for j in range(arr[i]):
        rain[j][i] = 1

answer = 0

for r in range(h):
    for c in range(w):
        if rain[r][c]:
            continue
        left_check = False
        right_check = False

        # left_check
        for i in range(c - 1, -1, -1):
            if rain[r][i] == 1:
                left_check = True
                break
        # right_check
        for i in range(c + 1, w):
            if rain[r][i] == 1:
                right_check = True
                break

        if left_check and right_check:
            answer += 1

print(answer)





