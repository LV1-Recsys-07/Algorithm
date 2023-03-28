
import sys
from collections import defaultdict, deque
n=int(sys.stdin.readline())
network=defaultdict(list)
for _ in range(int(sys.stdin.readline())):
    u, v= map(int, sys.stdin.readline().split())
    network[u-1].append(v-1)
    network[v-1].append(u-1)

q=deque([0]); visit=[0 for _ in range(n)]; cnt=0
while q:
    x=q.popleft()
    for y in network[x]:
        if not visit[y]:
            q.append(y)
            visit[y]=1
            cnt+=1
print(cnt-1)
