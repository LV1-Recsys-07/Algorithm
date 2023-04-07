import sys

s= sys.stdin.readline().strip()
board=[]
tmp=""
for i in range(len(s)):
    if s[i]==".":
        board.append(tmp)
        board.append(s[i])
        tmp=""
    else:
        tmp+=s[i]
board.append(tmp)

answer=[]
for s in board:
    if s==".":
        answer.append(s)
    else:
        n=len(s)
        if n and n%2:
            print(-1)
            break
        else:
            tmp=""
            while n:
                if n>=4:
                    tmp+="AAAA"
                    n-=4
                else:
                    tmp+="BB"
                    n-=2
            answer.append(tmp)
else:
    print("".join(answer))

            
