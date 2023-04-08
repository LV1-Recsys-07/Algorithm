import sys

n = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split())) 

if max(crane) < max(box) : 
    print(-1)
    sys.exit()
    
crane.sort(reverse = True)
box.sort(reverse = True)

count = 0

while box : 
    
    for i in crane : 
        for j in box :
            if i >= j :
                box.remove(j)
                break
                
    count += 1
    
print(count)