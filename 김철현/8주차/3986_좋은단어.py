import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
cnt = 0
for _ in range(n):
    arr = list(input().rstrip())
    m = len(arr)
    stack = []
    for i in range(m):
        if not stack:
            stack.append(arr[i])
        else:
            if arr[i] == stack[-1]:
                stack.pop()
            elif arr[i] != stack[-1]:
                stack.append(arr[i])

    if not stack:
        cnt += 1

print(cnt)






