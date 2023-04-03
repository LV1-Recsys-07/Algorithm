import sys
from collections import deque

n=int(sys.stdin.readline())  #board size
k=int(sys.stdin.readline())  #사과 개수
board=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    i, j=map(int, sys.stdin.readline().split())
    board[i-1][j-1]=1        #사과 위치 저장
l=int(sys.stdin.readline())  
route=deque(sys.stdin.readline().split() for _ in range(l))  #방향정보 저장

sec=0
x=y=0
board[x][y]=-1
snake=deque([(x, y)])  #뱀 위치 저장
dirx, diry=0, 1   

while True:
    sec+=1    
    nx=x+dirx
    ny=y+diry
    if 0<=nx<n and 0<=ny<n and board[nx][ny]!=-1:  #벽이 아니거나 자신이랑 부딪히지 않은 경우    
        x, y=nx, ny
        snake.appendleft((nx, ny))     #몸통 앞에 머리 저장
        if board[nx][ny]==0:  #사과가 없다면
            tx, ty=snake.pop()  #꼬리 줄이기
            board[tx][ty]=0     #board 갱신
        board[nx][ny]=-1        #머리부분
    else:
        print(sec)   #종료
        break
    if route and int(route[0][0])==sec:  #방향 변환
        dirx, diry=diry, dirx
        if route[0][1]=="D" and dirx==0:
            diry*=-1
        elif route[0][1]=="L" and diry==0:
            dirx*=-1
        route.popleft()
