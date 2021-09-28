import sys

def get_data():
  N = int(input())
  num_list = list(map(int ,input().split()))
  num_list.sort()

  return [N, num_list]


if __name__ == "__main__":
  N, num_list = get_data()
  last_num = -1
  min_check = sys.maxsize
  result = -1

  for num in num_list:
    if num == last_num: continue
    check = 0
    for other in num_list:
      check += abs(num-other)
      if check > min_check:
        break
    if check < min_check:
      min_check = check
      result = num
      last_num = num
  print(result)