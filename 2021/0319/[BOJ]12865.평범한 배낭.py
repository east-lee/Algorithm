def main():
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(K+1):
            w = arr[i][0]
            v = arr[i][1]
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(v+dp[i-1][j-w],dp[i-1][j])
    print(dp[-1][-1])



if __name__ == "__main__":
    N, K = map(int,input().split())
    arr = [[0,0]]
    for _ in range(N):
        arr.append(list(map(int,input().split()))) # w,v 순으로 저장

    main()

