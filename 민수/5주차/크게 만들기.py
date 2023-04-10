import sys

n, k = map(int, sys.stdin.readline().split())
number = sys.stdin.readline().rstrip()

stack = []
count = k # 없애야 할 숫자 개수

for i in range(n) : 
    while count > 0 and stack and stack[-1] < number[i] : # 스택에 있는 수보다 크다면
        stack.pop() # 스택에 있는 수 제거
        count -= 1 # count 감소
        
    stack.append(number[i]) # 스택에 넣기
    
print("".join(stack[:n - k])) # n - k 개의 수 출력
