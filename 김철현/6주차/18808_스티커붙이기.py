import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def rotate(ls):
    temp = []
    for x in zip(*ls[::-1]):
        temp.append(x)
    return temp

def check(ls):
    global r, c, sn, sm
    for i in range(sn):
        for j in range(sm):
            if 0 <= r + i < n and 0 <= c + j < m:
                if ls[i][j] and arr[r + i][c + j]:
                    return False
            else:
                return False
    return True

n, m, k = map(int, input().split())     # 세로, 가로, 스티거 개수
arr = [[False] * m for _ in range(n)]   # 전체 판

for _ in range(k):
    sn, sm = map(int, input().split())
    sticker = [list(map(int, input().rstrip().split())) for _ in range(sn)]

    flag = False
    for _ in range(4):
        for r in range(n):
            for c in range(m):
                sn = len(sticker)
                sm = len(sticker[0])
                if check(sticker):  # 스티커 붙이기
                    for i in range(sn):
                        for j in range(sm):
                            if sticker[i][j]:
                                arr[r + i][c + j] = True
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        sticker = rotate(sticker)

cnt = 0
for r in range(n):
    for c in range(m):
        if arr[r][c]:
            cnt += 1

print(cnt)