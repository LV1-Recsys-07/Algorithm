import sys
from collections import defaultdict

def check(cdt):

    dx=[-1, 0, 1, 0]
    dy=[0, -1, 0, 1]  

    cnt=defaultdict(lambda : [0,0])  #인접한 친구 수, 빈칸 수
    for x, y in cdt:
        for i in range(4):  #인접한 칸 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
                cnt[(nx, ny)][0]+=1 #친구 수 체크
                for j in range(4):  #인접한 칸 확인
                    nnx=nx+dx[j]
                    nny=ny+dy[j]
                    if 0<=nnx<n and 0<=nny<n and not board[nnx][nny]:   #빈칸 수 체크
                        cnt[(nx, ny)][1]+=1
    if cnt:
        return sorted(cnt.items(), key=lambda x : (-x[1][0],-x[1][1], x[0][0], x[0][1]))[0][0]

    m=-1
    ans=(-1, -1)
    for x in range(n):
        for y in range(n):
            if not board[x][y]:
                tmp=0
                for i in range(4):  #인접한 칸 중 빈칸 확인
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
                        tmp+=1
                if tmp>m:
                    m=tmp
                    ans=(x, y)
    return ans

def score():
    sc=0
    for k in like:
        cnt=0
        x, y=pos[k]
        for f in like[k]:
            fx, fy=pos[f]
            if abs(x-fx)+abs(y-fy)==1:
                cnt+=1
        if cnt:
            sc+=10**(cnt-1)
    return sc

n=int(sys.stdin.readline())
like=dict()
pos=dict()
board=[[0 for _ in range(n)] for _ in range(n)]

for _ in range(n**2):
    k, *v=map(int, sys.stdin.readline().split())
    like[k]=v

for k in like:  #좋아하는 친구 탐색
    cdt=[]
    for f in like[k]:
        fpos=pos.get(f, 0)
        if fpos:
            cdt.append(fpos)
    x, y=check(cdt)
    board[x][y]=k
    pos[k]=(x, y)
print(board)
print(score())