import sys

nn, mm, r=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(nn)]

def rotate(miter, n, m):
    for k in range(miter):
        i=j=k
        tmp=board[i][j]
        for j in range(k, m-k-1):  #좌
            board[i][j]=board[i][j+1]
        j+=1
        for i in range(k, n-k-1):  #상
            board[i][j]=board[i+1][j]
        i+=1
        for j in range(m-k-1, k, -1):  #우
            board[i][j]=board[i][j-1]
        j-=1
        for i in range(n-k-1, k, -1): #하
            board[i][j]=board[i-1][j]
        board[i][j]=tmp


for _ in range(r):
    rotate(min(nn, mm)//2, nn, mm)
for x in board:
    print(*x)
