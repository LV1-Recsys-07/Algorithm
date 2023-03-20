import sys

n, m = map(int, sys.stdin.readline().split())
train = [0] * n

for i in range(m) :
    op = list(map(int, sys.stdin.readline().split()))

    # 비트마스킹 사용 / tr : 기차 번호 / ch : 승객 위치
    
    if op[0] == 1 : # ch 좌석에 승객 태움
        tr = op[1] - 1
        ch = op[2] - 1
        
        train[tr] = train[tr] | 1 << ch   # ch 만큼 왼쪽으로 이동 후 or 연산 -> ch번째 자리에 1 생김

        
    elif op[0] == 2 :  # ch 좌석의 승객 하차
        tr = op[1] - 1
        ch = op[2] - 1
        
        train[tr] = train[tr] & ~(1 << ch)  # ch 만큼 이동 후 ~ 연산 -> ch번째 자리 빼고 모두 1로 채워짐 그 후 and 연산
        
    elif op[0] == 3 :  # 모두 한 칸씩 뒤로 이동
        tr = op[1] - 1
        
        train[tr] = (train[tr] << 1) & ~(1 << 20)  # 20번째 사람 하차
        
    else : # 모두 한  칸씩 앞으로 이동
        tr = op[1] - 1
        
        train[tr] = train[tr] >> 1 
        
print(len(set(train)))
