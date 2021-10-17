
def get_data():
  N, K = map(int, input().split())
  arr = list(int(input()) for _ in range(N))
  arr.sort()

  return [N, K, arr]

if __name__ == "__main__":
  N, K , arr = get_data()
  INF = 10001
  dp = [INF] * (K+1)
  dp[0] = 0

  for i in range(N):
    for j in range(arr[i], K+1):
      dp[j] = min(dp[j], dp[j-arr[i]] + 1)

  print(dp[-1] if dp[-1] != INF else -1)

