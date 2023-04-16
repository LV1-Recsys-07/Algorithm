import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


"""
idx     0 1 2 3
string  A C G T
"""

n, m = map(int, input().split())
counts = [[0, 0, 0, 0] for _ in range(m)]

stoi = {"A":0, "C":1, "G":2, "T":3}
itos = {0:"A", 1:"C", 2:"G", 3:"T"}
for _ in range(n):
    dna = input()
    for i in range(m):
        counts[i][stoi[dna[i]]] += 1

answer = ""
answer_cnt = 0
for i in range(m):
    max_cnt = 0
    idx = 0
    for j in range(4):
        if counts[i][j] > max_cnt:
            max_cnt = counts[i][j]
            idx = j
    answer_cnt += (n - max_cnt)
    answer += itos[idx]

print(answer)
print(answer_cnt)
