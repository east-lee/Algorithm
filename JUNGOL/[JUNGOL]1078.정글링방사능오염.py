testing = True
while testing:
    data = input()
    if not data:break
    m,n=map(int,data.split())
    check = list([0]*m for _ in range(n))
    arr = []

    for _ in range(n):
        input_data = list(map(int,input().split()))
        arr.append(input_data)

    first_x,first_y = map(int,input().split())
    first_x,first_y = first_x-1,first_y-1

    q = []
    q.append([first_y,first_x])
    next_q = []
    check[first_y][first_x] = 3
    direction = [[-1,0],[1,0],[0,1],[0,-1]]
    cnt = 1

    while q:
        y,x = q.pop()
        for k in range(4):
            i,j=y+direction[k][0],x+direction[k][1]

            if 0<=i<m and 0<=j<n and arr[i][j] == 1 and check[i][j]==0 and check[i][j]>cnt:
                check[i][j] = cnt+3
                arr[i][j] = 0
                next_q.append([i,j])
        if not q and next_q:
            cnt += 1
            q=next_q
    sur = 0
    result = cnt +3
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                sur +=1
    print(result)
    print(sur)




