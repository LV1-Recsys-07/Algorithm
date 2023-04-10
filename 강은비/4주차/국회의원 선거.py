import sys
import heapq                       #최대값을 계속 가져오기 위함

n=int(sys.stdin.readline())
dasom=int(sys.stdin.readline())
votes=[]
cnt=0

for _ in range(n-1):
    v=int(sys.stdin.readline())
    heapq.heappush(votes, (-v, v))   #가장 큰 값부터 앞에 오도록

if votes:
    while votes[0][1]>=dasom:        #가장 큰 투표수가 다솜이 보다 클 때
        _, v=heapq.heappop(votes)
        v-=1                         #다른 사람꺼 뺏어오기
        cnt+=1
        dasom+=1
        heapq.heappush(votes, (-v, v))
        
print(cnt)



