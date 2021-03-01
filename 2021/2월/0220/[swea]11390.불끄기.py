T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(list(input()) for _ in range(N))
    direction_go = [[0,1],[1,0]]
    direction_back = [[-1, 0], [0, -1]]

    max_y, max_x = 0,0
    min_result = N*M*2
    light_num = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '#':
                light_num += 1
                if i > max_y: max_y = i
                if j > max_x: max_x = j

    arr = arr[0:max_y+1]
    for i in range(len(arr)):
        arr[i] = arr[i][0:max_x+1]

    q = [[0,0,0,0,arr,0]]
    new_q = []
    while q:
        y,x,time,direction,past_arr,light_off_num = q.pop()
        if light_num == light_off_num and y == 0 and x == 0:
            min_result = time
            print(past_arr)
            break


        if not direction: direction_arr = direction_go
        else: direction_arr = direction_back

        for k in range(2):
            next_y,next_x = y+direction_arr[k][0],x+direction_arr[k][1]
            if 0<=next_y<len(arr) and 0<=next_x<len(arr[0]):
                new_arr = list([0]*len(arr[0]) for _ in range(len(arr)))
                for i in range(len(arr)):
                    for j in range(len(arr[0])):
                        new_arr[i][j] = past_arr[i][j]

                if new_arr[next_y][next_x] == '#':
                    new_arr[next_y][next_x] ='.'
                    if next_y == max_y and next_x == max_x:
                        new_q.append([next_y, next_x, time + 2,1,new_arr,light_off_num+1])
                    else: new_q.append([next_y,next_x,time+2,direction,new_arr,light_off_num+1])
                else:
                    if next_y == max_y and next_x == max_x:
                        new_q.append([next_y, next_x, time + 1, 1, new_arr,light_off_num])
                    else:
                        new_q.append([next_y, next_x, time + 1, direction, new_arr,light_off_num])

        if not q:
            q = new_q
            new_q = []


    print(f'#{t} {min_result}')




