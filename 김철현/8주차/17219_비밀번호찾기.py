import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


n, m = map(int, input().split())
dict = {}
for _ in range(n):
    site, pwd = input().rstrip().split()
    dict[site] = pwd

for _ in range(m):
    print(dict[input().rstrip()])