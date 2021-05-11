T = 10
for _ in range(1,T+1):
    t = int(input())
    arr = list(list(map(int,input().split())) for _ in range(100))
    start_x = 0
    start_y = 99
    for i in range(100):
        if arr[99][i] == 2:
            start_x = i
            break
    check = list([0]*100 for _ in range(100))

    direction = [[0,-1],[0,1],[-1,0]]
    check[start_y][start_x] = 1
    while True:
        for k in range(3):
            y,x=start_y+direction[k][0],start_x+direction[k][1]
            if 0<=y<100 and 0<=x<100 and arr[y][x] == 1 and check[y][x] == 0:
                check[y][x] = 1
                start_x,start_y = x, y
                break
        if start_y == 0:
            break

    print(f'#{t} {start_x}')