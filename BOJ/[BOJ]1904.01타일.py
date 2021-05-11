def main():
  DP = [0]*(N+1)
  for i in range(1,N+1):
    if i == 1: DP[i] = 1
    elif i == 2: DP[i] = 2
    else: DP[i] = (DP[i-1] + DP[i-2])%15746
  return DP[N]

if __name__ == "__main__":
  N = int(input())
  print(main())