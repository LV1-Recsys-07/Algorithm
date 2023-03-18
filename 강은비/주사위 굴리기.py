import sys

n, m ,x, y, k=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
order=map(int, sys.stdin.readline().split())
dir={1:(0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)}
dice={"top":0, "bottom":0, "front":0, "back":0, "left":0, "right":0}

def roll(k):     #주사위 상태 업데이트
    t, bt, r, l, f, bk = dice["top"], dice["bottom"], dice["right"], dice["left"], dice["front"], dice["back"]
    if k==1: #동
        dice["top"], dice["right"], dice["bottom"], dice["left"] = r, bt, l, t
    elif k==2: #서
        dice["top"], dice["left"], dice["bottom"], dice["right"] = l, bt, r, t
    elif k==3:  #북
        dice["top"], dice["back"], dice["bottom"], dice["front"] = f, t, bk, bt
        
    else: #남
        dice["top"], dice["front"], dice["bottom"], dice["back"] = bk, t, f, bt

    print(dice["top"])


for k in order:
    nx=x+dir[k][0]
    ny=y+dir[k][1]
    if 0<=nx<n and 0<=ny<m:
        roll(k)
        if not board[nx][ny]:
            board[nx][ny]=dice["bottom"]
        else:
            dice["bottom"]=board[nx][ny]
            board[nx][ny]=0
        x, y=nx, ny