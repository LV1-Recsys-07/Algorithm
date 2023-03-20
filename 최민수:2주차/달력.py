import sys
from collections import defaultdict

n = int(sys.stdin.readline())

vacation = defaultdict(int) # dictionary 생성

for i in range(n) :
    
    a, b = map(int, sys.stdin.readline().split())
    
    for i in range(a, b+1) :
        vacation[i] += 1
        
number = list(sorted(vacation.items())) # 키 값으로 딕셔너리 정렬

before = number[0][0] # 가로 시작점
height = number[0][1] # 세로 시작점

count = 1 # 초기값 설정
result = 0 # 최종 결과

for i in range(1, len(number)) :

    if number[i][0] - 1 == before : # 일정이 이어져 있다면
        count += 1
        height = max(height, number[i][1]) # 높이 갱신

        before = number[i][0] # 일정 이동

    else : # 일정이 이어져 있지 않다면
        result += count * height # 결과 업데이트
        
        # 초기값 업데이트

        count, height = 1, 0       
        height = max(height, number[i][1])
        before = number[i][0]

result += count * height # 결과 업데이트

print(result)