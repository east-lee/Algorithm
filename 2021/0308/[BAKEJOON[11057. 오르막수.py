n = int(input())
dp = [[0 for _ in range(10)]]
for i in range(1,n+1):
    dp_i = [0 for _ in range(10)]
    if i == 1:
        dp_i = [1 for i in range(10)]
    else:
        for j in range(10):
            dp_i[j] = sum(dp[-1][j:])
    dp.append(dp_i)
print(sum(dp[n])%10007)