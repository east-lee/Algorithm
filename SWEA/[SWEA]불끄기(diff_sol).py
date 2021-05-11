T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    room_info = list(list(input()) for _ in range(N))

    start_y, start_x = 0, 0

    check = [0]*N
    light_num = 0
    max_n = 0
    for i in range(N):
        for j in range(M):
            if room_info[i][j] == '#':
                check[i] = 1
                light_num += 1
                max_n = i
    room_info = room_info[:max_n+1]
    q = [[0,0,0,0,0]]
    new_q = []
    min_time = N*M*2
    while q:
        y,x,light_off_num,time,k = q.pop()
        if not y and not x and light_num == light_off_num:
            if min_time >time:
                min_time = time
            continue

        # 왼쪽 계단 -> 올라가던지 그층의 불을 끄던지 내려가던지
        now_off = light_off_num
        if not k and y+1 < len(room_info):
            if y+1 == M-1:
                new_q.append([y+1,x,light_off_num,time+1,1])
            else:
                new_q.append([y + 1, x, light_off_num, time + 1, 0])
        elif k and 0<y-1:
            new_q.append([y-1,x,light_off_num,time+1])


        check_off_time = 0
        for m in range(M):
            if room_info[y][m] == '#':
                check_off_time += 1
        if x == 0:
            new_q.append([y,M-1,light_off_num+check_off_time])
            now_off = light_off_num+check_off_time
        else:
            new_q.append([y,0,light_off_num+check_off_time])
            now_off = light_off_num + check_off_time

        if not q:
            q = new_q
            new_q = []


    print(f'#{t} {min_time}')










