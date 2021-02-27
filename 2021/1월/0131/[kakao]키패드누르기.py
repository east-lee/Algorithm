def solution(numbers, hand):
    answer = ''
    l_last =[3,0]
    r_last = [3,2]
    direction = [[0,1],[1,0],[-1,0],[0,-1]]
    check = [3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]
    for i in numbers:
        if i in [1,4,7,'*']:
            answer +='L'
            l_last = check[i]
        elif i in [3,6,9,'#']:
            answer += 'R'
            r_last = check[i]
        else:
            y,x = check[i]
            q = []
            q.append([y,x])
            new_q = []
            c = list([0]*3 for _ in range(4))
            l_check = 0
            r_check = 0
            while q:
                y,x = q.pop()
                for k in range(4):

                    next_y,next_x = y+direction[k][0],x+direction[k][1]
                    if 0<=next_y<4 and 0<=next_x<3 and c[next_y][next_x] == 0:
                        c[next_y][next_x]=1
                        new_q.append([next_y,next_x])
                if not q and new_q:
                    for yy,xx in new_q:
                        if l_last == [yy,xx]:
                            l_check = 1
                        if r_last == [yy,xx]:
                            r_check = 1
                    if r_check and l_check:
                        if hand == 'right':
                            answer+='R'
                            r_last = check[i]
                            break
                        else:
                            answer+='L'
                            l_last=check[i]
                            break
                    elif r_check:
                        answer += 'R'
                        r_last = check[i]
                        break
                    elif l_check:
                        answer += 'L'
                        l_last = check[i]
                        break
                    q=new_q
                    new_q = []
    return answer

