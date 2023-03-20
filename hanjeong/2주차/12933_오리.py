S = input()

s_dict = dict()
for idx, s in enumerate(S):
    if s in s_dict:
        s_dict[s].append(idx)
    else:
        s_dict[s] = [idx]

word = 'quack'
answer = []
flag = False
if 'q' in s_dict:
    while s_dict['q']:
        prev_min = -1
        start, end = 0, 0
        for w in word:
            if not w in s_dict or not s_dict[w]:
                flag = True
                break

            if s_dict[w] and min(s_dict[w]) < prev_min:
                while s_dict[w] and min(s_dict[w]) < prev_min:
                    s_dict[w].remove(min(s_dict[w]))
                if not s_dict[w]:
                    flag = True
                    break
                prev_min = min(s_dict[w])
                s_dict[w].remove(min(s_dict[w]))
            else:
                prev_min = min(s_dict[w])
                s_dict[w].remove(min(s_dict[w]))

            if w == 'q':
                start = prev_min

            if w == 'k':
                end = prev_min
                answer.append([start,end])
        if flag:
            break

if answer and len(S) == len(answer)*5:
    end_list = [answer[0][1]]
    for i in range(1, len(answer)):
        for j in range(len(end_list)):
            if answer[i][0] > end_list[j]:
                end_list[j] = answer[i][1]
                break
        else:
            end_list.append(answer[i][1])
    print(len(end_list))
else:
    print(-1)
