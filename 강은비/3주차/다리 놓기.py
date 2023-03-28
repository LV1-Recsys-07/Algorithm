import sys

def bridge(n, m):
    dp=[[0 for _ in range(m)] for _ in range(n)]  #dp[i][j] -> 서쪽의 i번째 사이트가 동쪽의 j번째 사이트에 연결될 수 있는 방법의 수
    for i in range(n):                                     #-> i-1번째 사이트가 1부터 j-1번째 사이트에 연결될 수 있는 총 방법의 수
        for j in range(m):
            if i==0 or i==j: #첫번째 사이트 / i==j 로 연결되는 경우는 순서대로 맵핑되는 경우 1가지 밖에 없음
                dp[i][j]=1
            elif j>i:        #본인i 보다 큰 j로만 가서 안겹치도록 
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1]  #앞 사이트 i-1이 j-1로 연결되는 방법 
    print(dp)
    return sum(dp[n-1])

t=int(sys.stdin.readline())
for _ in range(t):
    n, m=map(int, sys.stdin.readline().split())
    print(bridge(n, m))