import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

stack = [0]
answer = 0
for i in range(n):
    cur = arr[i][1]             # 현재 높이
    if cur > stack[-1]:         # 마지막 보다 높다면 삽입
        stack.append(cur)
    else:
        while cur < stack[-1]:  # 현재높이보다 큰 애들은 전부 pop
            stack.pop()
            answer += 1
        if stack[-1] != cur:    # 같을 경우 같은 라인에 존재하기 때문에 다를 경우만 삽입
            stack.append(cur)


while stack[-1]:                # 0으로 끝나지 않은 경우 stack에 남아있는 높이 개수를 더해줌
    stack.pop()
    answer += 1

print(answer)
