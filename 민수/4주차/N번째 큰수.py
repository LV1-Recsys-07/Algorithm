import sys
import heapq

n = int(sys.stdin.readline()) 
number = []

for i in range(n) : 
    temp = list(map(int, sys.stdin.readline().split())) # 한 줄씩 입력 받아옴
    for j in temp :
        if len(number) < n : # n 보다 number라는 배열이 짧다면
            heapq.heappush(number, j)
            
        elif number[0] < j : # 더 작은 값이 있다면 가장 작은 값 빼고 새로운 값 push
            heapq.heappop(number)
            heapq.heappush(number, j)
            
print(number[0]) 
