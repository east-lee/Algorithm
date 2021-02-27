def checking(y,x,N):
    global result_blue,result_white
    if N == 1:
        if arr[y][x] == 0 : result_white+=1
        else: result_blue += 1
        return

    dividing = False
    first_color = arr[y][x]
    for i in range(y,y+N):
        for j in range(x,x+N):
            if first_color != arr[i][j]:
                dividing=True
                break
        if dividing: break
    if not dividing:
        if first_color == 1:result_blue+=1
        else: result_white +=1
    else:
        N = N//2
        y1,x1 = y,x
        y2,x2 = y,x+N
        y3,x3 = y+N,x
        y4,x4 = y+N,x+N
        checking(y1,x1,N)
        checking(y2, x2, N)
        checking(y3, x3, N)
        checking(y4, x4, N)




testing = True
while testing:
    n = int(input())
    if not n:break
    arr = list(list(map(int,input().split())) for _ in range(n))
    result_white = 0
    result_blue = 0
    start_y, start_x, N = 0,0,n
    checking(start_y,start_x,N)
    print(result_white)
    print(result_blue)