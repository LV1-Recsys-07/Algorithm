import sys

n = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split())) 

if max(crane) < max(box) :  # 크레인이 들 수 있는 무게보다 박스가 무겁다면
    print(-1)
    sys.exit()
    
# 내림차순 정렬

crane.sort(reverse = True) 
box.sort(reverse = True)

count = 0

while box : # 박스가 남아 있다면
    
    for i in crane : 
        for j in box : 
            if i >= j : # 들 수 있으면
                box.remove(j)
                break
                
    count += 1
    
print(count)
