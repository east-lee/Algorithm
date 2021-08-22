import sys

def get_data():
  N = int(input())
  arr = list(map(int, input().split()))
  arr.sort()

  return [N, arr]


if __name__ == "__main__":
  N, arr = get_data()
  result = [sys.maxsize, 0, 0]
  left, right = 0, N-1

  while left < right:
    left_num, right_num = arr[left], arr[right]
    mix_num = left_num + right_num
    # print(mix_num, left_num, right_num)
    if result[0] > abs(mix_num):
      result = [abs(mix_num), left_num, right_num]

    if mix_num < 0:
      left += 1
    elif mix_num > 0:
      right -= 1
    else:
      break

  print(result[1], result[2])
