def solution():
  dp = [[0]*max_n for _ in range(max_n)]

  for i in range(1,max_n):
    dp[0][i] = 1

  for i in range(1, max_n):
    for j in range(i, max_n):
      dp[i][j] = dp[i-1][j] + dp[i][j-1]

  return dp




if __name__ == "__main__":
  max_n = 31
  dp = solution()

  # for d in dp: print(d)

  while True:
    n = int(input())
    if not n: break

    print(dp[n][n])

