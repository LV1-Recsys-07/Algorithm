import sys
from collections import deque

n=int(sys.stdin.readline())
cnt=0
for _ in range(n):
    s=sys.stdin.readline().strip()
    if len(s)%2:
        continue
    else:
        q=deque()
        for x in s:
            if q and q[-1]==x:
                q.pop()
            else:
                q.append(x)
        if not q:
            cnt+=1
print(cnt)



