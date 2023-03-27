N, M = map(int, input().split())

trains = [[0 for _ in range(20)] for _ in range(N)]
for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        if not trains[command[1]-1][command[2]-1]:
            trains[command[1]-1][command[2]-1] = 1
    elif command[0] == 2:
        if trains[command[1]-1][command[2]-1]:
            trains[command[1]-1][command[2]-1] = 0
    elif command[0] == 3:
        for i in range(19, 0, -1):
            trains[command[1]-1][i] = trains[command[1]-1][i-1]
        trains[command[1]-1][0] = 0
    else:
        for i in range(19):
            trains[command[1]-1][i] = trains[command[1]-1][i+1]
        trains[command[1]-1][19] = 0

trains = set(tuple(train) for train in trains) # 중복 제거. 이차원 리스트 바로 set으로 안 바뀜.

print(len(trains))