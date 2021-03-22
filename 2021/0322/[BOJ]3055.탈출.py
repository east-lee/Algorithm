def main(arr, start, end,water):
    result = "KAKTUS"
    check = list([0]*C for _ in range(R))
    check[start[0]][start[1]] = 1
    q = [start]
    if water:
        water_q = water
    else:
        water_q = []
    new_q, water_new_q = [[] for _ in range(2)]
    cnt = 0
    while q:
        i,j = q.pop()

        if end == [i,j]:
            result = cnt
            break
        while water_q:
            y,x = water_q.pop()
            for k in range(4):
                new_y,new_x = y+direction[k][0], x+direction[k][1]
                if 0<=new_y<R and 0<=new_x<C and arr[new_y][new_x] == ".":
                    arr[new_y][new_x] = "*"
                    water_new_q.append([new_y,new_x])

        for k in range(4):
            ni, nj = i+direction[k][0], j+direction[k][1]
            if 0<=ni<R and 0<=nj<C and check[ni][nj] == 0 and (arr[ni][nj] == "D" or arr[ni][nj] =="."):
                check[ni][nj] = 1
                new_q.append([ni,nj])

        if not q and new_q:

            q = new_q
            water_q = water_new_q
            new_q=[]
            water_new_q = []
            cnt += 1
    print(result)



if __name__ == "__main__":
    R, C = map(int,input().split())
    arr = list(list(input()) for _ in range(R))
    start_point, end_point, water = list([] for _ in range(3))
    direction = [[-1,0],[1,0],[0,-1],[0,1]]


    for i in range(R):
        for j in range(C):
            if arr[i][j] == "D":
                end_point = [i,j]
            elif arr[i][j] == "S":
                start_point = [i,j]
            elif arr[i][j] == "*":
                water.append([i,j])

    main(arr,start_point,end_point,water)