import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node, depth):
    d[node] = depth
    for nxt in graph[node]:
        dfs(nxt, depth + 1)
    return

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


T = int(input())
for _ in range(T):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    d = [0] * (n + 1)
    parent = [0] * (n + 1)
    for _ in range(n - 1):
        p, c = map(int, input().split())
        parent[c] = p
        graph[p].append(c)

    root = 0

    for i in range(1, n + 1):
        if parent[i] == 0:
            root = i
            break
    dfs(root, 0)
    a, b = map(int, input().split())
    print(lca(a, b))