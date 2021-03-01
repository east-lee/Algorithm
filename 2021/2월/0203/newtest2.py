def solution(y,x):
    global left_check,right_check,x_check,y_check
    y_can_check,x_can_check,right_can_check,left_can_check = True,True,True,True
    y_result,x_result,right_result,left_result = 0,0,0,0
    y_list,x_list,right_list,left_list = [],[],[],[]
    if y_check[y][x] == 0:
        i,j = y,x
        while True:
            if 0<=i<h and 0<=j<w:
                y_list.append([i,j])
                y_check[i][j] = 1
                if arr[i][j] == 1:
                    y_can_check = False
                i += 1
            else: break
    if x_check[y][x] == 0:
        i,j = y,x
        while True:
            if 0<=i<h and 0<=j<w:
                x_list.append([i, j])
                x_check[i][j] = 1
                if arr[i][j] == 1:
                    x_can_check = False
                j += 1
            else: break
    if right_check[y][x] == 0:
        i,j = y,x
        while True:
            if 0<=i<h and 0<=j<w:
                right_list.append([i, j])
                if arr[i][j] == 1:
                    right_can_check = False
                right_check[i][j] = 1
                i += 1
                j += 1
            else: break
    if left_check[y][x] == 0:
        i,j = y,x
        while True:
            if 0<=i<h and 0<=j<w:
                left_list.append([i, j])
                if arr[i][j] == 1:
                    left_can_check = False
                left_check[i][j] = 1
                i -=1
                j -=1
            else: break
    last_list= []
    if y_can_check:
        check_result = []
        for i in range(len(home)):
            m,n = home[i]
            r_check = w*h
            for j in range(len(y_list)):
                r = abs(m-y_list[j][0]) + abs(n-y_list[j][1])
                if r < r_check:
                    r_check = r
            check_result.append(r_check)
        y_result = min(check_result)
        last_list.append(y_result)
    if x_can_check:
        check_result = []
        for i in range(len(home)):
            m,n = home[i]
            r_check = w*h
            for j in range(len(x_list)):
                r = abs(m-x_list[j][0]) + abs(n-x_list[j][1])
                if r < r_check:
                    r_check = r
            check_result.append(r_check)
        x_result = min(check_result)
        last_list.append(x_result)
    if right_can_check and len(right_list) > 1:
        check_result = []
        for i in range(len(home)):
            m,n = home[i]
            r_check = w*h
            for j in range(len(right_list)):
                r = abs(m-right_list[j][0]) + abs(n-right_list[j][1])
                if r < r_check:
                    r_check = r
            check_result.append(r_check)
        right_result = min(check_result)
        last_list.append(right_result)
    if left_can_check and len(left_list) > 1:
        check_result = []
        for i in range(len(home)):
            m,n = home[i]
            r_check = w*h
            for j in range(len(left_list)):
                r = abs(m-left_list[j][0]) + abs(n-left_list[j][1])
                if r < r_check:
                    r_check = r
            check_result.append(r_check)
        left_result = min(check_result)
        last_list.append(left_result)

    if right_can_check or left_can_check or x_can_check or y_can_check:
        return min(last_list)
    else:
        return False



T = int(input())
for t in range(1,T+1):
    w,h = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(h))
    right_check = list([0]*w for _ in range(h))
    left_check = list([0] * w for _ in range(h))
    x_check = list([0] * w for _ in range(h))
    y_check = list([0] * w for _ in range(h))
    result = w*h
    home = []

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                home.append([i,j])
    can_do = 0
    for i in range(h):
        for j in range(w):
            semi_result = solution(i,j)
            if semi_result and semi_result < result:
                result = semi_result
                can_do = 1
    if can_do:
        print(f'#{t} {result}')
    else:
        print(f'#{t} -1')
