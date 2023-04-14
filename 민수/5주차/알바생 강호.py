import sys

n = int(sys.stdin.readline())
people = []

for i in range(n) :  # people 이라는 리스트에 팁 append
    temp = int(sys.stdin.readline())
    people.append(temp)
    
people.sort(reverse = True) # 내림차순 정렬 (가장 최대의 팁을 얻기 위해)

result = 0

for i in range(n) :
    temp = people[i] - i
    
    if temp <= 0 :  # 0 이하면 반복문 종료
        break
        
    result += temp
        
print(result)
