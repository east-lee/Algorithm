def get_data():
  N = int(input())
  arr = list(map(int, input().split()))

  return [N, arr]


def make_sub_arr(k=0):
  global check_list, check_sum

  if k == N:
    check_list[check_sum] = True
    return
  
  check_sum += arr[k]
  make_sub_arr(k+1)

  check_sum -= arr[k]
  make_sub_arr(k+1)

if __name__ == "__main__":
  N, arr = get_data()
  check_list = [False] * (100000 * N + 1)
  check_sum = 0
  make_sub_arr()

  for num in range(len(check_list)):
    if not check_list[num]:
      print(num)
      break