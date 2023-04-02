import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

stack = [0]
answer = 0
for i in range(n):
    cur = arr[i][1]
    if cur > stack[-1]:
        stack.append(cur)
    else:
        while cur < stack[-1]:
            stack.pop()
            answer += 1
        if stack[-1] != cur:
            stack.append(cur)


while stack[-1]:
    stack.pop()
    answer += 1

print(answer)
