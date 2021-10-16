def get_data():
  N = int(input())
  arr = list(map(int, input().split()))

  return [N, arr]

if __name__ == "__main__":
  N, arr = get_data()
  dp = [1] * N

  for i in range(1, N):
    for j in range(i):
      if arr[j] > arr[i]:
        dp[i] = max(dp[i], dp[j]+1)

  print(max(dp))