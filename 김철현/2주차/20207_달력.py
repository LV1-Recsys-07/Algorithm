import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())

ls = []
for _ in range(n):
    a, b = map(int, input().split())
    ls.append((a, b))

ls.sort(key=lambda x: (x[0], -x[1]))

arr = [0] * 366
for a, b in ls:
    for i in range(a, b + 1):
        arr[i] += 1

width = 0
height = 0
answer = 0

for i in range(1, 366):
    if arr[i]:
        width += 1
        height = max(height, arr[i])
    else:
        answer += width * height
        width = 0
        height = 0

answer += width * height    # 마지막 일정이 차있어서 초기화가 안된경우

print(answer)
