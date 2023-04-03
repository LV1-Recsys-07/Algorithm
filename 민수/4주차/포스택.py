import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

flag = 1
stacks = [[0] for i in range(4)] 

for i in range(n) :
    min_diff = float('inf')
    temp = -1 
    
    for j in range(4) :
        stk = stacks[j]
        if stk[-1] < array[i] :
            diff = array[i] - stk[-1]
            if diff < min_diff :
                min_diff = diff
                temp = j
                
    if temp != -1 :
        stacks[temp].append(array[i])
        
    else : 
        flag = 0
        break
        
if flag :
    print("YES")
    
else :
    print("NO")