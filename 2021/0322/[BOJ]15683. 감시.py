import copy

def solution(direction_arr):
    global arr,result
    check = copy.deepcopy(arr)

    for i in range(len(direction_arr)):
        y, x, cctv_num = cctv_point[i]
        for k in CCTV[cctv_num][direction_arr[i]]:
            start_y,start_x = y,x
            while 0<=start_y<N and 0<=start_x<M and arr[start_y][start_x] != 6:
                check[start_y][start_x] = "#"
                start_y, start_x = start_y+Direction[k][0], start_x +Direction[k][1]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if check[i][j] == 0:
                cnt += 1
    if cnt < result:
        result = cnt

def main(k,n,cctv_direction_arr):
    if k == n:
        solution(cctv_direction_arr)
        return

    for i in range(len(CCTV[cctv_point[k][2]])):
        cctv_direction_arr[k] = i
        main(k+1,n,cctv_direction_arr)
        cctv_direction_arr[k] = -1


if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(N))
    result = N*M
    Direction = [[-1,0],[0,1],[1,0],[0,-1]]

    CCTV = [
        [],
        [[0],[1],[2],[3]], #1번 CCTV 는 네방향으로 가능
        [[0,2],[1,3]], #2번 CCTV는 위아래 혹은 오른쪽왼쪽
        [[0,1],[1,2],[2,3],[3,0]], #3번 CCTV 직각
        [[3,0,1],[0,1,2],[1,2,3],[2,3,0]], # 4번
        [[0,1,2,3]] # 5번 전방향
    ]

    cctv_point = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and arr[i][j] != 6:
                cctv_point.append([i,j,arr[i][j]])

    cctv_direction_arr = [-1]*len(cctv_point)

    main(0,len(cctv_point),cctv_direction_arr)

    print(result)