import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
LOG = 20

# 깊이 구하는 함수
def depth(x, h):
    c[x] = True
    d[x] = h
    for y in graph[x]:
        if c[y]:
            continue
        parent[y][0] = x
        depth(y, h + 1)

# 부모 관계 설정 함수
def set_parent():
    depth(1, 0)
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# 공통조상 구하기
def lca(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]



n = int(input())
parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
# parent[i][j] : i번 노드의 2**j 번째 부모(첫번째 부모: j=0)
d = [0] * (n + 1) # 노드까지의 depth 정보
c = [0] * (n + 1) # 노드의 depth가 계산되었는지 여부

graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))


