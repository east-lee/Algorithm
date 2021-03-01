T = int(input())
for t in range(1,T+1):
    W, H =map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(H))
    home = []
    x_check = [0]*W
    y_check = [0]*H
    right_check = list([0]*W for _ in range(H)) #왼쪽위에서오른쪽아래로가는대각선 체크
    left_check = list([0] * W for _ in range(H)) #오른쪽위에서 왼쪽아래로 가는 대각서 체크

    result = W*H
    can_make = False
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1:
                home.append([i,j])
                y_check[i] = 1
                x_check[j] = 1
    y_result = 0
    x_result = 0
    right_result = 0
    left_result = 0
    for i in range(H):
        for j in range(W):
            if j==0 and y_check[i] == 0: #y=m 방향으로 검사
                can_make=True
                for m in range(H):
                    if y_check[m] == 1 and y_result < abs(m-i):
                        y_result = abs(m-i)
            if i==0 and x_check[j] == 0:
                can_make = True
                for m in range(W):
                    if x_check[m] == 1 and x_result < abs(m-j):
                        x_result = abs(m-j)
            if right_check[i][j] == 0 and arr[i][j]==0:
                y,x = i, j
                right_check[i][j] = 1
                check_list = [[i,j]]
                breaker = False
                while True:
                    next_y, next_x = y+1, x+1
                    if 0<=next_y<H and 0<=next_x<W and arr[next_y][next_x] == 0:
                        check_list.append([next_y,next_x])
                        y, x = next_y,next_x
                    elif 0<=next_y<H and 0<=next_x<W and arr[next_y][next_x] ==1:
                        breaker = True
                        break
                    else:
                        break
                if not breaker and len(check_list) > 1:
                    can_make = True
                    cc = [0]*len(home)
                    for m in range(len(home)):
                        cnt = 0
                        check_i, check_j = home[m]
                        for l in range(len(check_list)):
                            check_ii, check_jj = check_list[l]
                            if abs(check_i-check_ii)+abs(check_j-check_jj) > cnt:
                                cnt = abs(check_i-check_ii)+abs(check_j-check_jj)
                        cc[m] = cnt
                    if right_result < max(cc):
                        right_result = max(cc)

            if left_check[i][j] == 0 and arr[i][j] == 0:
                y, x = i, j
                left_check[i][j] = 1
                check_list = [[i, j]]
                breaker = False
                while True:
                    next_y, next_x = y - 1, x - 1
                    if 0 <= next_y < H and 0 <= next_x < W and arr[next_y][next_x] == 0:
                        check_list.append([next_y, next_x])
                        y, x = next_y, next_x
                    elif 0<=next_y<H and 0<=next_x<W and arr[next_y][next_x] == 1:
                        breaker = True
                        break
                    else:
                        break
                if not breaker and len(check_list) > 1:
                    can_make = True
                    cc = [0] * len(home)
                    for m in range(len(home)):
                        cnt = 0
                        check_i, check_j = home[m]
                        for l in range(len(check_list)):
                            check_ii, check_jj = check_list[l]
                            if abs(check_i - check_ii) + abs(check_j - check_jj) > cnt:
                                cnt = abs(check_i - check_ii) + abs(check_j - check_jj)
                        cc[m] = cnt
                    if left_result < max(cc):
                        left_result = max(cc)
    if can_make:
        prinf(x_result,y_result,left_result,right_result)
    else:
        result = -1
    print(f'#{t} {result}')




