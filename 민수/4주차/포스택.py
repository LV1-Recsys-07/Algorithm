import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split())) # 순열

flag = 1
stacks = [[0] for i in range(4)] # 4개의 스택 생성

for i in range(n) :
    min_diff = float('inf') # 차이를 무한으로 가정
    temp = -1 
    
    for j in range(4) : # 스택 4개 돌면서
        stk = stacks[j]
        if stk[-1] < array[i] : # 가장 차이가 적게 나는 스택 찾기
            diff = array[i] - stk[-1]
            if diff < min_diff :
                min_diff = diff
                temp = j
                
    if temp != -1 : # 찾았다면 append
        stacks[temp].append(array[i])
        
    else :  # 아닐 경우에는 flag 설정
        flag = 0
        break
        
if flag :
    print("YES")
    
else :
    print("NO")
