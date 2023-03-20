import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

def solve():
    q = deque()
    q.append(1)         # 1번부터 시작
    visited[1] = True   # 1번 방문 처리
    cnt = 0             # 바이러스에 걸리게 되는 수
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                cnt += 1
    return cnt


n = int(input())    # 컴퓨터 수
m = int(input())    # 연결되어 있는 쌍의 수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
print(solve())