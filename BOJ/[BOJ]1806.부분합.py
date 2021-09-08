import sys

def get_data():
  N, S = map(int, input().split())
  arr = list(map(int, input().split()))

  return [N, S, arr]


if __name__ == "__main__":
  N, S, arr = get_data()
  min_length = sys.maxsize
  sub_sum = arr[0]
  left, right = [0 for _ in range(2)]

  while left <= right and right < N :
    if sub_sum <= S and right+1 < N:
      right += 1
      sub_sum += arr[right]
    elif sub_sum > S:
      left += 1
      sub_sum -= arr[left-1]
    else:
      right += 1
    min_length = min(min_length, right - left + 1) if sub_sum >= S else min_length

  print(min_length) if min_length < sys.maxsize else print(0)