import sys
sys.stdin = open("input.txt")

'''
내림차순 정렬 후
크레인을 기준으로 돌면서 박스 하나씩 제거
크레인의 첫번째 원소가 박스의 첫번째 원소보다 작으면 -1
'''

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
answer = 0
if crane[0] < box[0]:
    answer = -1
else:
    while box:
        for i in range(n):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        answer += 1

print(answer)
