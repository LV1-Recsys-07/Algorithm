import sys

n=int(sys.stdin.readline())   #크레인 개수 
w=list(map(int, sys.stdin.readline().split()))    #크레인당 무게
m=int(sys.stdin.readline())   #박스 개수 
box=list(map(int, sys.stdin.readline().split()))  #박스당 무게 

w.sort(reverse=True)
box.sort(reverse=True)
t=0
 
if box[0]>w[0]:      #박스 최대가 크레인 최대 무게보다 클 때
    print(-1)
else:
    while box:  #못 옮긴 박스가 있을 때 까지
        for x in w:
            for i in range(len(box)):
                if x >= box[i]:
                    box.pop(i)
                    break
        t+=1
    print(t)
    


