def dfs(k, junction_cell, junction, check):
    global result_junction, result_junction_cell
    if k==len(check_cell):
        if result_junction_cell < junction_cell:
            result_junction_cell = junction_cell
            result_junction = junction
        elif result_junction_cell == junction_cell and junction < result_junction:
            result_junction = junction
        return
    #
    # if result_junction == len(check_cell) and junction > result_junction:
    #     return
    if junction_cell + (len(check_cell)-k)+1 < result_junction_cell:
        return
    y,x = check_cell[k]
    for m in range(4):
        next_y, next_x = y+direction[m][0],x+direction[m][1]
        check_copy = list([0]*N for _ in range(N))
        c = list([0]*N for _ in range(N))
        breaker = False
        junction_check = junction
        for i in range(N):
            for j in range(N):
                check_copy[i][j] = check[i][j]
                c[i][j] = check[i][j]
        while True:
            if 0<=next_y<N and 0<=next_x<N and not arr[next_y][next_x] and not check_copy[next_y][next_x]:
                check_copy[next_y][next_x] = 1
                junction_check += 1
            else:
                breaker = True
                break
            if next_y == 0 or next_y ==(N-1) or next_x ==0 or next_x==(N-1):
                dfs(k+1,junction_cell+1, junction_check,check_copy)
                break
            next_y += direction[m][0]
            next_x += direction[m][1]
        if breaker:
            dfs(k+1,junction_cell,junction,c)

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(list(map(int,input().split())) for _ in range(N))
    check = list([0]*N for _ in range(N))
    check_cell = []
    result_junction_cell = 0
    result_junction = N*N
    direction = [[-1,0],[0,-1],[1,0],[0,1]]
    for i in range(N):
        for j in range(N):
            if (not i or not j or i==(N-1) or j==(N-1)) and arr[i][j]:
                check[i][j] = 1
                arr[i][j] = 0
            elif arr[i][j]:
                check_cell.append([i,j])

    dfs(0,0,0,check)

    print(f'#{t} {result_junction}')


