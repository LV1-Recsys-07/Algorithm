import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


s = list(input().rstrip())
n = len(s)
cnt = 0
for i in range(n):
    if s[i] == "X":
        s[i] = "A"
        cnt += 1
    else:
        if cnt:
            if cnt % 4 == 0:
                continue
            elif cnt % 2 == 0:
                s[i - 1] = "B"
                s[i - 2] = "B"
            else:
                print(-1)
                exit()
            cnt = 0
    if i == n - 1:
        if cnt:
            if cnt % 4 == 0:
                continue
            elif cnt % 2 == 0:
                s[i] = "B"
                s[i - 1] = "B"
            else:
                print(-1)
                exit()
print("".join(s))



