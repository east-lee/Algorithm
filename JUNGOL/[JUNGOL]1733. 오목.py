T = 9
for _ in range(T):
    arr = list(list(map(int,input().split())) for _ in range(19))
    detecting_num = 0
    direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    result_y, result_x = 0, 0
    last_y,last_x = 0,0
    for i in range(19):
        for j in range(19):
            if arr[i][j]:
                for k in range(8):
                    y,x = i+direction[k][0], j+direction[k][1]
                    if 0<=y<19 and 0<=x<19 and arr[y][x] == arr[i][j]:
                        checking_num = 2
                        q = []
                        q.append([y,x])
                        while q:
                            next_y, next_x = q.pop()
                            next_y += direction[k][0]
                            next_x += direction[k][1]
                            if 0 <= next_y < 19 and 0 <= next_x < 19 and arr[next_y][next_x] == arr[i][j]:
                                checking_num +=1
                                q.append([next_y,next_x])
                        if checking_num == 5:
                            detecting_num = arr[y][x]
                            result_y,result_x = i,j
                            last_y,last_x = i+direction[k][0]*4,j+direction[k][1]*4
                            break
            if detecting_num:break
        if detecting_num: break
    if detecting_num:
        print(detecting_num)
        if last_x < result_x:
            print(last_y+1,last_x+1)
        else:
            print(i + 1, j + 1)
    else:
        print(0)



