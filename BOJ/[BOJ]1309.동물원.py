# 0 => 1 / 1 => 3 / 2 => 7 / 3 => 17

if __name__ == "__main__":
  N = int(input())
  dp = [0 for _ in range(N+1)]
  dp[0], dp[1] = 1, 3

  mod_num = 9901

  for i in range(2, N + 1):
    dp[i] = dp[i-2] + (dp[i-1] * 2)
    dp[i] = dp[i] % mod_num

  print(dp[N])