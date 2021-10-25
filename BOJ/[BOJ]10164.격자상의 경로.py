if __name__ == "__main__":
    N, M, K = map(int, input().split())

    dp = [[0] * (M) for _ in range(N)]
    num = 0
    dp[0][0] = 1
    check_y, check_x = 0, 0
    for i in range(N):
        for j in range(M):
            num += 1
            if num == K:
                check_y, check_x = [i, j]
            if i == 0 and j == 0:
                continue

            num_up = dp[i-1][j] if 0<=i-1 else 0
            num_left = dp[i][j-1] if 0<=j else 0
            dp[i][j] = num_up + num_left
    # for d in dp:print(d)
    # print(check_y, check_x)

    if not K:
        print(dp[N-1][M-1])
    else:
        print(dp[check_y][check_x] * dp[N-check_y-1][M-check_x-1])



