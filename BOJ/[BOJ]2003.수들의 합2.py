

def get_data():
  N, M = map(int, input().split())
  arr = list(map(int,input().split()))
  return [N, M, arr]


if __name__ == "__main__":
  N, M, arr = get_data()
  left, right = 0, 0
  cnt = 0
  check_sum = 0
  while left<=right and right<N:
    if check_sum <= M:
      if check_sum == M:
        cnt += 1
      check_sum += arr[right] if right < N else 0
      right += 1


    elif check_sum > M:
      left += 1
      check_sum -= arr[left-1]

  print(cnt)