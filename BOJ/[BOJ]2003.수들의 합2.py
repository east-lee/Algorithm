def get_data():
  N, M = map(int, input().split())
  arr = list(map(int,input().split()))
  return [N, M, arr]


if __name__ == "__main__":
  N, M, arr = get_data()
  left, right = 0, 0
  cnt = 0

  while left<=right and right <= N:
    check_sum = sum(arr[left:right])
    cnt += 1 if check_sum == M else 0

    if check_sum <= M:
      right += 1
    elif check_sum > M and left < right:
      left += 1
    else:
      right += 1
      left += 1

  print(cnt)