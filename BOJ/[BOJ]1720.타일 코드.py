def main():
  dp = [0]*(N+1)
  dp[0] = 1
  for i in range(1,N+1):
    if i == 1: dp[i] = 1
    else:
      dp[i] = dp[i-1]+dp[i-2]*2

  if N % 2 :
    return (dp[N] + dp[(N-1)//2]) / 2
  else:
    return (dp[N]+dp[N//2]+dp[(N-2)//2]*2)/2

if __name__ == "__main__":
  N  = int(input())
  print(int(main()))