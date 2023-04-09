import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().rstrip()))
stack = [num[0]]
for i in range(1, n):
    while stack and num[i] > stack[-1] and k:
        stack.pop()
        k -= 1
    stack.append(num[i])

while k:
    stack.pop()
    k -= 1
for x in stack:
    print(x, end="")

