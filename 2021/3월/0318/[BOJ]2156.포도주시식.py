n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

dp = [0]*(n+1)

for i in range(1,n+1):
    if i == 1: dp[1] = arr[1]
    elif i== 2: dp[2] = dp[1]+arr[2]
    else:
        dp[i] = max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i],dp[i-1])
print(dp[n])
