import sys

n = int(sys.stdin.readline())

stack = []
result = 0

for i in range(n) : 
    x, y = map(int, sys.stdin.readline().split()) # 좌표 받아오기
    while stack and y < stack[-1] : # stack이 비어있지 않고 현재 좌표보다 높다면 pop
        result += 1
        stack.pop()
    if stack and y == stack[-1] : # 현재 높이와 같다면 넘어가기
        continue 
        
    stack.append(y) # continue에서 걸리지 않는다면 append
    
while stack : # 남아 있는 건물 확인
    if stack[-1] > 0 :
        result += 1
    
    stack.pop()
        
print(result)
