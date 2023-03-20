N = int(input())

schedules = []
for _ in range(N):
    schedules.append(list(map(int, input().split()))) 

schedules.sort(key=lambda x: (x[0], -x[1]+x[0]))

sch_dict = dict()
for sch in schedules:
    r = 1
    if sch[0] in sch_dict:
        while True:
            if r not in sch_dict[sch[0]]:
                break
            else:
                r += 1
        sch_dict[sch[0]].append(r)
    else:
        sch_dict[sch[0]] = [1]
    
    for i in range(sch[0]+1, sch[1]+1):
        if i in sch_dict:
            sch_dict[i].append(r)
        else:
            sch_dict[i] = [r]

x, y = 0, 0
prev_key = 0
answer = 0
for key, value in sch_dict.items():
    if key == prev_key + 1:
        x += 1
        if max(value) > y:
            y = max(value)
    else:
        answer += x*y
        x = 1
        y = max(value)
    prev_key = key

print(answer + x*y)
