T = int(input())
for t in range(1,T+1):
    w,h = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(h))
    init_list = list([0]*w for _ in range(h))
    check = [list([0]*w for _ in range(h)),list([0]*w for _ in range(h)),list([0]*w for _ in range(h)),list([0]*w for _ in range(h))]
    home = []
    can_do = False
    result = w*h
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:home.append([i,j])

    direction = [[1,0],[0,1],[1,1],[1,-1]]

    for i in range(h):
        for j in range(w):
            for k in range(4):
                check_list = check[k]
                can_make = True
                road_list = []
                if not check_list[i][j]:
                    road_list.append([i,j])
                    y, x= i, j
                    check_list[y][x] = 1
                    if arr[y][x] == 1:
                        can_make = False
                    while True:
                        y, x= y+direction[k][0],x+direction[k][1]
                        if 0<=y<h and 0<=x<w:
                            check_list[y][x] = 1
                            road_list.append([y,x])
                            if arr[y][x] == 1:
                                can_make = False
                        else:
                            break

                    if can_make and len(road_list)>1:
                        can_do = True
                        home_dist = [0]*len(home)
                        for m in range(len(home)):
                            semi_r = w * h
                            for l in range(len(road_list)):
                                a,b,c,d = home[m][0], home[m][1], road_list[l][0], road_list[l][1]
                                r = abs(a-c) + abs(b-d)
                                if r < semi_r:
                                    semi_r = r
                            home_dist[m] = semi_r
                        if max(home_dist) < result:
                            print(i,j,k,road_list)
                            result = max(home_dist)


    if can_do:
        print(f'#{t} {result}')
    else:
        print(f'#{t} -1')
