import sys

wb=[]
while True:
    try:
        w, b=map(int, sys.stdin.readline().split())
        wb.append([w, b])   #백, 흑 점수
    except:
        break
              
dp=[[0 for _ in range(16)] for _ in range(16)]  #백 i, 흑 j

for white, black in wb:
    for i in range(15, -1, -1):
        for j in range(15, -1, -1):   #k번째 사람까지 보았을때, 백이 i명, 흑이 j명 있을 때 
            if i>0:
                dp[i][j]=max(dp[i][j], dp[i-1][j]+white)    #영입x, 백으로 영입
            if j>0:
                dp[i][j]=max(dp[i][j], dp[i][j-1]+black)    #영입x, 흑으로 영입
print(dp)

'''
for white, black in wb:
    for i in range(16):
        for j in range(16):   #k번째 사람까지 보았을때, 백이 i명, 흑이 j명 있을 때 
            if i<15:
                dp[i+1][j]=max(dp[i+1][j], dp[i][j]+white)
            if j<15:
                dp[i][j+1]=max(dp[i][j+1], dp[i][j]+black)  #이미 포함된게 또 포함됨
    print(dp)

print(dp)
'''