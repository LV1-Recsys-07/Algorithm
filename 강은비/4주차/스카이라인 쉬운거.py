import sys

n=int(sys.stdin.readline())
height=[]
cnt=0

for _ in range(n):
    _, y = map(int, sys.stdin.readline().split())
    while height and y<height[-1]:     #y가 작은 경우 -> 스카이라인이 끊기는 지점
        cnt+=1                         #빌딩 수 +=1
        height.pop(-1)        
    if y!=0 and (not height or height[-1]!=y):   #0이 아니거나 현재 top과 같지 않은 경우 추가
        height.append(y)

print(cnt+len(height))  #남아있는 빌딩 수 추가