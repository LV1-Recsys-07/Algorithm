import sys

n=int(sys.stdin.readline())
a=map(int, sys.stdin.readline().split())
stlast=[-1, -1, -1, -1]   #각 stack의 top 저장

for x in a:
    for i in range(4):
        if x>stlast[i]:   #top보다 클 경우에만 갱신
            stlast[i]=x
            break
    else:                 #모든 stakc의 top보다 작다면 출력시 작은게 먼저 나오므로 불가능
        print("NO")
        break
else:                     #모든 수가 스택에 순서대로 들어갔을 때 
    print("YES")
