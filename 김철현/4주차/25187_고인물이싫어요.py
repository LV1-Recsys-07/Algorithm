import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


'''
n: 물탱크의 수 
m: 파이프의 수
q: 물탱크에 방문할 횟수
'''

def find(x):
    if x != parent[x]:
        return find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
        water[x] += water[y]
    else:
        parent[x] = y
        water[y] += water[x]

n, m, q = map(int, input().split())
arr = [0] + list(map(int, input().rstrip().split()))    # 청정수: 1 고인물: 0
water = [0] * (n + 1)
for i in range(1, n + 1):
    if arr[i]:
        water[i] = 1    # 청정수이면 1로
    else:
        water[i] = -1   # 고인물이면 -1로
parent = [i for i in range(n + 1)]  # 부모 배열 초기화
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):          # 루트 노드가 다를 경우
        union(a, b)


for _ in range(q):
    v = int(input())            # 방문할 물탱크 번호
    if water[find(v)] > 0:      # 루트 노드 물탱크만 보면 됨
        print(1)
    else:
        print(0)
