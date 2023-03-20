import sys

word = sys.stdin.readline().rstrip()

if len(word) % 5 != 0 :
    print(-1)
    sys.exit()
    
visited = [0] * len(word)  # 방문 표시하는 리스트 생성
count = 0

for i in range(len(word)) :
    if word[i] == 'q' and visited[i] == 0 : # q로 시작하고 방문한 곳인지 확인
        target = 'quack' # target 단어
        k = 0
        flag = 1
        
        for j in range(i, len(word)) :
            if word[j] == target[k] and visited[j] == 0 :
                visited[j] = 1
                
                if word[j] == 'k' : # 오리 체크 후 flag = 0 으로 설정
                    if flag :
                        count += 1
                        flag = 0
                        
                    k = 0
                    continue
                    
                k += 1

if not all(visited) or count == 0 :
    print(-1)
    
else :
    print(count)     