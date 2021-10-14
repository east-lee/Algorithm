if __name__ == "__main__":
  n = int(input())
  dp = [0] * (n+1)
  dp[0] = 1

  num = 1
  while num <= n:
    for i in range(num, n+1):
      dp[i] += dp[i-num]

    num *= 2

  print(dp[n] % 1000000000)




