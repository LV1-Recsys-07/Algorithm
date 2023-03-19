import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

arr = list(input().rstrip())
n = len(arr)
visited = [False] * n
duck = ["q", "u", "a", "c", "k"]
answer = 0

for start in range(n):
    if visited[start]:
        continue
    idx = 0  # 울음소리를 트래킹
    check = False
    for i in range(start, n):
        if visited[i]:
            continue
        if arr[i] == duck[idx]:
            visited[i] = True
            idx += 1

            if idx == 5:
                check = True
                idx = 0

    if check:
        answer += 1
    if idx or not visited[start]:
        print(-1)
        exit()

print(answer)
