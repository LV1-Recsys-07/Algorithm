import sys

n = int(sys.stdin.readline())
people = []

for i in range(n) :
    temp = int(sys.stdin.readline())
    people.append(temp)
    
people.sort(reverse = True)

result = 0

for i in range(n) :
    temp = people[i] - i
    
    if temp <= 0 :
        break
        
    result += temp
        
print(result)