import sys

n, k = map(int, sys.stdin.readline().split())
number = sys.stdin.readline().rstrip()

stack = []
count = k

for i in range(n) : 
    while count > 0 and stack and stack[-1] < number[i] : 
        stack.pop()
        count -= 1
        
    stack.append(number[i])
    
print("".join(stack[:n - k]))