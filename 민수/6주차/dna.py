import sys

n, m = map(int, sys.stdin.readline().split())
dna = [sys.stdin.readline().rstrip() for i in range(n)]

dna.sort()
result = ''

for i in range(m) : 
    
    seq = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
    
    for j in range(n) : 
        temp = dna[j][i]
        seq[temp] += 1
        
    result += max(seq, key = seq.get)
    
answer = 0
for i in range(n) :
    for j in range(m) : 
        if result[j] != dna[i][j] : 
            answer += 1
            
print(result)
print(answer)