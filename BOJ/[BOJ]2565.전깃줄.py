


def get_data():
  N = int(input())
  arr = [
    list(map(int, input().split())) for _ in range(N)
  ]

  arr.sort(key=lambda x:x[0])

  return [N,arr]


if __name__ == "__main__":
  N, arr = get_data()
  dp = [0 for _ in range(N)]
  arr_check = []

  for i in range(N):
    arr_check.append(arr[i][1])

  for i in range(N):
    for j in range(i):
      if arr_check[i] > arr_check[j] and dp[i] < dp[j]:
        dp[i] = dp[j]
    dp[i] += 1
  print(N-max(dp))
