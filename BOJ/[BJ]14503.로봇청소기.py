def main():
    global arr, d, r, c, result
    cnt = 0
    for k in range(1,5):
        new_d = (d+k)%4
        next_y, next_x = r+direction[new_d][0], c + direction[new_d][1]
        if 0<=next_y<N and 0<=next_x<M and arr[next_y][next_x] ==0:
            r,c = next_y, next_x
            d = new_d
            arr[next_y][next_x] = 2
            result += 1
            main()
            break
        else:
            cnt += 1
    if cnt == 4:
        next_y, next_x = r-direction[d][0], c-direction[d][1]
        if 0<=next_y<N and 0<=next_x<M and arr[next_y][next_x] != 1:
            r,c = next_y,next_x
            main()
        else:
            return

if __name__ == "__main__":
    N,M = map(int,input().split())
    # 북쪽 : 0 / 동족: 1 / 남쪽 2/ 서쪽 3
    r, c, d = map(int,input().split())
    result = 1
    # 북쪽 : 0 / 동족: 1 / 남쪽 2/ 서쪽 3  > 북:0 / 서: 1 / 남 : 2 / 동: 3
    if d == 1: d = 3
    elif d == 3: d = 1

    direction = [[-1,0], [0,-1], [1,0], [0,1]]
    arr = list(list(map(int,input().split())) for _ in range(N))
    arr[r][c] = 2
    main()
    # for i in arr:
    #     print(i)
    print(result)