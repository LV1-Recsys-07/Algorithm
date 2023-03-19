import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

'''
1 i x: i번째 기차의 x번째 좌석에 사람 태우기
2 i x: i번째 기차의 x번째 좌석의 사람 하차
3 i: i번째 기차에 앉아있는 승객들 모두 한칸씩 뒤로
4 i: i번째 기차에 앉아있는 승객들 모두 한칸씩 앞으로 
'''

n, m = map(int, input().split())
train = [0 for _ in range(n)]

for _ in range(m):
    cmd = list(map(int, input().rstrip().split()))
    if cmd[0] == 1:
        train[cmd[1] - 1] |= (1 << (cmd[2] - 1))
    elif cmd[0] == 2:
        train[cmd[1] - 1] &= ~(1 << (cmd[2] - 1))
    elif cmd[0] == 3:
        train[cmd[1] - 1] <<= 1
        train[cmd[1] - 1] &= ~(1 << 20) # 자리수 맞춤
    elif cmd[0] == 4:
        train[cmd[1] - 1] >>= 1


print(len(set(train)))