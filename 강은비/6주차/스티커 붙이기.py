import sys

def rotate(sn, sm, sticker, cnt):  #가장 첫 행이 마지막 열로
    rsticker=[[0 for _ in range(sn)] for _ in range(sm)]
    for i in range(sn):
        for j in range(sm):
            rsticker[j][-i-1]=sticker[i][j]
    return find(sm, sn, rsticker, cnt+1)

def find(sn, sm, sticker, cnt):
    global total
    x=y=-1
    for i in range(n):         #시작점 찾기
        for j in range(m):
            flag=True
            for si in range(sn):
                for sj in range(sm):
                    if i+si<n and j+sj<m and (sticker[si][sj]==0 or nb[i+si][j+sj]==0):
                        continue
                    else:
                        flag=False
                        break  #스티커 붙이기 불가능
                if not flag:
                    break
            else:
                x,y=i, j
                for si in range(sn):        #찾은 시작점에서 붙이기
                    for sj in range(sm):
                        if sticker[si][sj]==1:
                            nb[x+si][y+sj]=1
                            total+=1
                return 
    else:
        if cnt<3:          
            rotate(sn, sm, sticker, cnt)     #90도씩 회전 시키기
        else:
            return 

n, m, k=map(int, sys.stdin.readline().split())
nb=[[0 for _ in range(m)] for _ in range(n)]
total=0
for _ in range(k):
    sn, sm=map(int, sys.stdin.readline().split())
    sticker=[list(map(int, sys.stdin.readline().split())) for _ in range(sn)]
    find(sn, sm, sticker, 0)     #스티커 붙일 수 있는지 탐색
print(total)
