import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    log = input().rstrip()
    # 커서를 기준으로 양옆으로
    left = []
    right = []
    for x in log:
        if x == "<":
            if left:
                s = left.pop()
                right.append(s)
        elif x == ">":
            if right:
                s = right.pop()
                left.append(s)
        elif x == "-":
            if left:
                left.pop()
        else:
            left.append(x)

    right = reversed(right)
    left.extend(right)
    print("".join(left))
