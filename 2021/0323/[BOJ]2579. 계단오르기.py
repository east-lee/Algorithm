# 실패했었던 문제! 다시 풀어봄

n = int(input())
arr = list(int(input()) for _ in range(n))
dp = [0]*(n+1)
arr.insert(0,0)
for i in range(1,n+1):
  if i == 1:
    dp[1] = arr[1]
  elif i == 2:
    dp[2] = arr[1] + arr[2]
  elif i == 3:
    dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])
  elif i>=4:
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
print(dp[n])
