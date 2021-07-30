def find_num(num):
  for i in range(len(num_list)):
    if num_list[i] > num + 1:
      return i
  return "not"

def main():
  global arr_dict

  result = []
  check_index = 0
  check_num = num_list[check_index]
  cnt = 0

  while check_index < N:
    cnt += 1
    if check_num + 1 not in num_list or ((check_num + 1) in num_list and arr_dict[str(check_num+1)] == 0):
      while arr_dict[str(check_num)]:
        arr_dict[str(check_num)] -= 1
        result.append(check_num)
      check_index += 1
      if check_index == len(num_list):
        break
      check_num = num_list[check_index]
    else:
      next_num_index = find_num(check_num)

      if next_num_index != "not":
        while arr_dict[str(check_num)]:
          arr_dict[str(check_num)] -= 1
          result.append(check_num)
        arr_dict[str(num_list[next_num_index])] -= 1
        result.append(num_list[next_num_index])
        check_index += 1
        if check_index == len(num_list):
          break
        check_num = num_list[check_index]
      else:
        result.append(check_num + 1)
        arr_dict[str(check_num+1)] -= 1

  result = list(map(str,result))

  return ' '.join(result)


def get_data():
  N = int(input())
  arr = list(map(int, input().split()))
  arr_dict = {}
  num_list = []

  arr.sort()

  for num in arr:
    if str(num) in arr_dict.keys():
      arr_dict[str(num)] += 1
    else:
      arr_dict[str(num)] = 1
      num_list.append(num)

  num_list.sort()

  return [N, arr, arr_dict, num_list]


if __name__ == "__main__":
  N, arr, arr_dict, num_list = get_data()
  print(main())

