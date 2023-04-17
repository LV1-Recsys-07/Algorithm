import sys

n, m, k = map(int, sys.stdin.readline().split())

notebook = [[0] * m for i in range(n)]
sticker = []

for i in range(k) : 
    r, c = map(int, sys.stdin.readline().split())
    temp = [list(map(int, sys.stdin.readline().split())) for i in range(r)]
    sticker.append(temp)

def rotate(sticker) : 
    c, r = len(sticker), len(sticker[0])
    result = [[0] * c for l in range(r)]
    
    for i in range(r) :
        for j in range(c) :
            result[i][j] = sticker[c-j-1][i]

    return result

def check(x, y, sticker) : 
    r, c = len(sticker), len(sticker[0])
    
    for i in range(r) :
        for j in range(c) :
            if sticker[i][j] == 1 and notebook[x + i][y + j] == 1 :
                return False
            
    return True

for st in sticker : 
    way = 1  
    while True : 
        flag = 0 
        r, c = len(st), len(st[0])
        for i in range(n - (r - 1)) :
            for j in range(m - (c - 1)) : 
                if check(i, j, st) :
                    for row in range(r) :
                        for col in range(c) :
                            if st[row][col] == 1 :
                                notebook[i + row][j + col] = 1
                            
                    flag = 1
                    break
                    
            if flag :
                break
                
        if not flag : 
            if way == 0 :
                break
                
            st = rotate(st)
            way = (way + 1) % 4
        
        elif flag :
            break
            
count = 0

for i in range(n) :
    for j in range(m) :
        if notebook[i][j] == 1 :
            count += 1

print(count)   