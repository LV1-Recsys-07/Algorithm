import sys

a, b=map(int, sys.stdin.readline().split())
cnt=0

while b>=a:
    if b==a:
        print(cnt+1)
        break
    if b%10==1:
        b-=1
        b/=10
    else:
        b/=2
    cnt+=1
else:
    print(-1)