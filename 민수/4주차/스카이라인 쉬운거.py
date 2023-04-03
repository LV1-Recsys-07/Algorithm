import sys

n = int(sys.stdin.readline())

stack = []
result = 0

for i in range(n) : 
    x, y = map(int, sys.stdin.readline().split())
    while stack and y < stack[-1] :
        result += 1
        stack.pop()
    if stack and y == stack[-1] :
        continue 
        
    stack.append(y)
    
while stack :
    if stack[-1] > 0 :
        result += 1
    
    stack.pop()
        
print(result)