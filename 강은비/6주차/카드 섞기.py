import sys
from collections import deque

n=int(sys.stdin.readline())
answer=deque(map(int, sys.stdin.readline().split()))

def shuffle(k):
    for i in range(1, k+2):
        if i==1:           #첫 단계
            tmp=deque()
            for _ in range(2**k):
                x=cards.pop()
                tmp.append(x)
        else:
            rest=deque()
            for _ in range(2**(k-i+1)):
                x=tmp.popleft()       #이전에 뽑았던 것들에서 뽑기
                rest.append(x)        #현재 단계에서 뽑은 것들 저장
            cards.extendleft(tmp)
            tmp=rest
    cards.extendleft(tmp)   #마지막에 남은 거 맨 위에 올려놓기 
    #print(k, cards)    

for i in range(1, 10):   
    for j in range(1, 10):        
        if 2**i<n and 2**j<n:
            cards=deque(range(1, n+1))    
            shuffle(i)   #첫번째K
            shuffle(j)   #두번째K
        if cards==answer:
            print(i, j)
            sys.exit()