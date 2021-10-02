


def get_data():
  N = int(input())
  arr = list(map(int, input().split()))

  return [N, arr]


if __name__ == "__main__":
  N, arr = get_data()
  dp = [0 for _ in range(N)]
  dp[0] = arr[0]

  for i in range(1,N):
    s = []
    for j in range(i-1, -1,-1):
      if arr[i] > arr[j]: s.append(dp[j])

    if not s:
      dp[i] = arr[i]
    else:
      dp[i] = arr[i] + max(s)
  print(max(dp))





