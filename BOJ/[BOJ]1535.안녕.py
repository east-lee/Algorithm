def get_data():
  N = int(input())
  health, happy = (
    list(map(int,input().split())) for _ in range(2)
  )

  return [N, health, happy]

if __name__ == "__main__":
  N, health, happy = get_data()
  M = 101
  dp = [
    [0] * M for _ in range(N+1)
  ]

  for i in range(1,N+1):
    for j in range(M-1):
      if j < health[i-1]:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-health[i-1]] + happy[i-1] )

  print(dp[N][M-2])
