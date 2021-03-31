n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
dp = [0]*(n+1)

for i in range(1,n+1):
    if dp[i-1]<=0:
        dp[i] = arr[i]
    else:
        dp[i] = arr[i]+dp[i-1]
print(max(dp[1:]))
