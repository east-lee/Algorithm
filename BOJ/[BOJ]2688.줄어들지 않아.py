def DP(n):
  dp = [
    [0] * 10 for _ in range(n+1)
  ]

  # 초기화
  for i in range(10):
    dp[1][i] = 1

  for i in range(2,n+1):
    pre_sum = sum(dp[i-1])
    for j in range(10):
      if j == 0:
        dp[i][j] = pre_sum
      else:
        dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

  print(sum(dp[n]))

if __name__ == "__main__":
  TC = int(input())

  for _ in range(TC):
    n = int(input())
    DP(n)