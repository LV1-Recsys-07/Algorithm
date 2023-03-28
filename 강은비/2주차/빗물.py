import sys
from collections import deque

h, w=map(int, sys.stdin.readline().split())
ground=list(map(int, sys.stdin.readline().split()))

st=deque()
rain=0
for i in range(w):    
    while st and ground[i]>=ground[st[-1]]:      # i 보다 높이가 낮은 경우 
        now=st.pop()                             # 빗물이 고일 수 있는 위치
        nowh=ground[now]
        if st:
            rain+=(min(ground[st[-1]], ground[i])-nowh)*(i-st[-1]-1)  # now 위치에서의 빗물 구하기 / now 전과 now 이후 높이 비교
    st.append(i)

print(rain)