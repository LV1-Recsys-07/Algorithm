import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
stack = [[], [], [], []]

"""
무조건 stack 최상단 수보다 큰수를 삽입해야함
"""
check = True
for x in arr:
    for i in range(4):
        if not stack[i]:
            stack[i].append(x)
            break
        else:
            if stack[i][-1] < x:
                stack[i].append(x)
                break
    else:
        check = False
        break

if check:
    print("YES")
else:
    print("NO")


