def main():
  dp = [0] * (N+1)

  for i in range(1, N+1):
    if i == 1:
      dp[1] = 0
    elif i == 2:
      dp[i] = 1
    else:
      dp[i] = (i-1) * (dp[i-1] + dp[i-2]) % 1000000000

  print(dp[N])


if __name__ == "__main__":
  N = int(input())
  main()