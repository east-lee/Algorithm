def main():
    dp = [0]*(N+1)
    for i in range(N+1):
        if i == 1: dp[i] = 0
        elif i == 2: dp[i] = 1
        else:
            dp[i] = dp[i-1]+1
            if i%3 ==0:
                dp[i] = min(dp[i],dp[i//3]+1)
            if i% 2 == 0:
                dp[i] = min(dp[i],dp[i//2]+1)


    print(dp[N])
    # print(dp)

if __name__ == "__main__":
    N = int(input())
    main()