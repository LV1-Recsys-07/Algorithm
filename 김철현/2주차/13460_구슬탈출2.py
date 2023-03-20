import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque


def solve(r_red, c_red, r_blue, c_blue):
    q = deque()
    q.append((r_red, c_red, r_blue, c_blue, 0))
    visited.append((r_red, c_red, r_blue, c_blue))
    while q:
        r_red, c_red, r_blue, c_blue, cnt = q.popleft()
        if arr[r_red][c_red] == "O":
            if cnt <= 10:
                return cnt
            else:
                return -1
        if cnt >= 10:
            continue

        for k in range(4):
            nr_red, nc_red, nr_blue, nc_blue = r_red, c_red, r_blue, c_blue
            while True:
                nr_red += dr[k]
                nc_red += dc[k]
                if arr[nr_red][nc_red] == "#":
                    nr_red -= dr[k]
                    nc_red -= dc[k]
                    break
                if arr[nr_red][nc_red] == "O":
                    break

            while True:
                nr_blue += dr[k]
                nc_blue += dc[k]
                if arr[nr_blue][nc_blue] == "#":
                    nr_blue -= dr[k]
                    nc_blue -= dc[k]
                    break
                if arr[nr_blue][nc_blue] == "O":
                    break

            if arr[nr_blue][nc_blue] == "O":            # 파란공이 빠진경우
                continue

            if nr_red == nr_blue and nc_red == nc_blue: # 같은 위치에 있는경우
                d_red = abs(nr_red - r_red) + abs(nc_red - c_red)
                d_blue = abs(nr_blue - r_blue) + abs(nc_blue - c_blue)

                if d_red > d_blue:
                    nr_red -= dr[k]
                    nc_red -= dc[k]
                else:
                    nr_blue -= dr[k]
                    nc_blue -= dc[k]

            if (nr_red, nc_red, nr_blue, nc_blue) not in visited:
                visited.append((nr_red, nc_red, nr_blue, nc_blue))
                q.append((nr_red, nc_red, nr_blue, nc_blue, cnt + 1))

    return -1

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
visited = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == "R":
            rr = i
            cr = j
        elif arr[i][j] == "B":
            rb = i
            cb = j

print(solve(rr, cr, rb, cb))
