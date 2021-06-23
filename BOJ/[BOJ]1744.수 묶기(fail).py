def N_less_3():
  if num_list[1] > 0:
    return num_list[1] * num_list[2] + num_list[0]
  elif num_list[1] < 0:
    return num_list[1] * num_list[0] + num_list[2]
  else:
    return sum(num_list)

def main():
  return_result = 0

  if N <= 3:
    return N_less_3()

  left, right = 0, N-1

  while left < right:
    left_num_1, left_num_2, right_num_1, right_num_2 = num_list[left], num_list[left+1], num_list[right], num_list[right - 1]
    # print(left_num_1,left_num_2,right_num_1,right_num_2,left,right)
    left_check, right_check = False, False
    if left_num_1 < 0 and left_num_1 * left_num_2 > 0 and left+1 < right-1:
      return_result += left_num_1 * left_num_2
      next_left = left + 2
    else: left_check = True

    if right_num_1 > 0 and right_num_1 * right_num_2 > 0 and left+1 < right-1:
      return_result += right_num_1 * right_num_2
      next_right = right - 2
    else: right_check = True

    if left_check and right_check:
      break

    if not left_check: left = next_left
    if not right_check: right = next_right

  if left < right:
    print(left,right)
    for i in range(left, right+1):
      return_result += num_list[i]
  return return_result

def get_data():
  N = int(input())
  num_list = []

  for _ in range(N):
    num_list.append(int(input()))

  num_list.sort()

  return [N, num_list]

if __name__ == "__main__":
  N, num_list = get_data()

  result = main()
  print(result)