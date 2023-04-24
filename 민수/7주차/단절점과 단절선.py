import sys

n = int(sys.stdin.readline())

matrix = [[] for i in range(n + 1)]

for i in range(n - 1) : 
    a, b = map(int, sys.stdin.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)
    
    
def vertex(x) : 
    if len(matrix[x]) <= 1 :
        print("no")
        
    else : 
        print("yes")
        
    
m = int(sys.stdin.readline())

for i in range(m) : 
    a, b = map(int, sys.stdin.readline().split())
    
    if a == 1 :
        vertex(b)
        
    else : 
        print("yes")   