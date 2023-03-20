N = int(input())
M = int(input())

snail = [[0 for _ in range(N)] for _ in range(N)]

next = N**2
r, c = 0, 0
status = 'b'
answer = [0, 0] # 인덱스 에러 방지

while next != 1:
    if status == 'b':
        while 0 <= r < N-1 and 0 <= c < N and snail[r+1][c] == 0:
            if next == M:
                answer = [r+1, c+1]
            snail[r][c] = next
            r += 1
            next -= 1
        status = 'r'
    elif status == 'r':
        while 0 <= r < N and 0 <= c < N-1 and snail[r][c+1] == 0:
            if next == M:
                answer = [r+1, c+1]
            snail[r][c] = next
            c += 1
            next -= 1   
        status = 'u'
    elif status == 'u':
        while 1 <= r < N and 0 <= c < N and snail[r-1][c] == 0:
            if next == M:
                answer = [r+1, c+1]
            snail[r][c] = next
            r -= 1
            next -= 1        
        status = 'l'
    else:
        while 0 <= r < N and 1 <= c < N and snail[r][c-1] == 0:
            if next == M:
                answer = [r+1, c+1]
            snail[r][c] = next
            c -= 1
            next -= 1
        status = 'b'

snail[N//2][N//2] = 1
if M == 1:
    answer = [N//2+1, N//2+1]

for row in snail:
    for i in row:
        print(i, end=" ")
    print()
print(answer[0], answer[1])
