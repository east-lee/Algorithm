def get_data():
  N, M = map(int,input().split())
  arr = [
    list(input()) for _ in range(N)
  ]

  K = int(input())

  return [N, M, K, arr]

if __name__ == "__main__":
  N, M, K, arr = get_data()
  result = [0] * N
  for i in range(N):
    zero_cnt = arr[i].count('0')

    if K%2 and zero_cnt%2 and zero_cnt<=K:
      for j in range(N):
        result[i] += 1 if arr[i] == arr[j] else 0
    elif K%2 and not zero_cnt%2 and zero_cnt <= K:
      for j in range(N):
        result[i] += 1 if arr[i] == arr[j] else 0
  print(max(result))