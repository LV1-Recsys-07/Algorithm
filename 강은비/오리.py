import sys

def check(sound):
    cnt={v:i for i, v in enumerate("quack")}
    for s in sound:
        i=cnt[s]
        for d in range(len(ducks)):
            if (i==0 and ducks[d][-1]==str(4)) or ducks[d][-1]==str(i-1):    #순서에 맞는 다음 글자이거나 다 울고 새로 울때 글자 추가
                ducks[d]+=str(i)
                break
        else:
            if i==0:                  #새로운 오리가 울 때
                ducks.append(str(i))
            else:
                return -1 
                
sound=sys.stdin.readline().strip()
ducks=[]
k=check(sound)
if k:
    print(k)
else:
    for d in ducks:
        if not d.endswith('4'): #끊긴 경우 
            print(-1)
            break
    else:
        print(len(ducks))

        
                
