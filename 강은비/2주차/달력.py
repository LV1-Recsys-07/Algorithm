import sys

calender=[0 for _ in range(366)]
n=int(sys.stdin.readline())
start=366
for _ in range(n):
    s, e=map(int, sys.stdin.readline().split())
    for i in range(s, e+1):
        calender[i]+=1        #해당 일자에 일정이 있는 만큼 더해줌

total=0
h=0
cnt=0
for j in range(366):
    if calender[j]==0:   #코팅지 자름
        total+=h*(cnt)
        h=0
        cnt=0
    if calender[j]!=0:
        h=max(calender[j], h)
        cnt+=1
total+=h*(cnt)     #마지막 일정
print(total)
