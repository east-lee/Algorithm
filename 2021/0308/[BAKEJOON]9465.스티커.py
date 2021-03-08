T = int(input())
for _ in range(T):
    n = int(input())

    arr = []
    for _ in range(2):
        input_list = list(map(int,input().split()))
        input_list.insert(0,0)
        arr.append(input_list)

    dp = [[0]*(n+1) for _ in range(2)]

    for i in range(1,n+1):
        if i == 1:
            dp[0][i] = arr[0][i]
            dp[1][i] = arr[1][i]
        else:

            dp[0][i] = max(dp[1][i-1],dp[1][i-2])+arr[0][i]
            dp[1][i] = max(dp[0][i-1],dp[0][i-2])+arr[1][i]
    print(max(dp[0][n],dp[1][n]))

