import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
ls = [i for i in range(n)]
cur = 0
step = 1
while len(ls) >= 2:
    cur = (cur + step ** 3 - 1) % len(ls)
    ls.remove(ls[cur])
    step += 1

print(ls[0] + 1)
