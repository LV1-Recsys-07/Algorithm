import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input().rstrip()) for _ in range(n)], reverse=True)
answer = 0
for i in range(n):
    tip = arr[i] - i
    if tip < 0:
        tip = 0
    answer += tip

print(answer)