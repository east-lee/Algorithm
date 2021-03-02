n = int(input())
dp =[0]*(n+1)
dp[0] = 0
for i in range(1,n+1):
    if i == 1 or i == 2: dp[i] = 1
    else:
        dp[i] = dp[i-1]+dp[i-2]
print(dp[-1])

