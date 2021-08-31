if __name__ == "__main__":
  N = int(input())
  if N%2: print(0)
  else:
    MAX_N = 31
    dp = [0 for _ in range(MAX_N + 1)]
    dp[2] = 3

    for i in range(4, 31):
      if i % 2: continue
      dp[i] = dp[2]*dp[i-2]
      for j in range(4, i, 2):
        dp[i] += (2 * dp[i-j])
      dp[i] += 2
    print(dp[N])



