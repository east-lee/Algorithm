


for _ in range(int(input())):
    dp = [0, 1, 1, 1, 2, 2, 3]
    n = int(input())
    if n <=6:
        print(dp[n])
    else:
        for i in range(7,n+1):
            appended_num = dp[-1]+dp[i-5]
            dp.append(appended_num)
        print(dp[n])
        
