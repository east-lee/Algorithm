# 참고한 반례
# 10
# -5
# -4
# -3
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# output: 65
# 5
# 1
# 1
# 1
# 1
# 1
# output:5

def right_search():
  global num_list
  right_result = 0
  while len(num_list) > 1:
    right_num_1, right_num_2 = num_list[-2], num_list[-1]
    sum_right = right_num_1 + right_num_2
    check_right = right_num_1 * right_num_2
    if right_num_1 <= 0 or right_num_2 <=0:break
    right_result += check_right if check_right > sum_right else sum_right
    num_list = num_list[:-2]

  return right_result

def left_search():
  global num_list
  left_result = 0

  while len(num_list) > 1:
    left_num_1, left_num_2 = num_list[0], num_list[1]
    sum_left = left_num_2 + left_num_1
    check_left = left_num_2 * left_num_1

    if left_num_1 >= 0 or left_num_2 > 0: break
    left_result += check_left if check_left > sum_left else sum_left
    num_list = num_list[2:]

  return left_result


def main():
  return_result = 0
  return_result += right_search()
  return_result += left_search()
  return_result += sum(num_list)

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
  if N >= 3:
    result = main()
  elif N == 2:
    result = sum(num_list) if sum(num_list) > num_list[0] * num_list[1] else num_list[0]*num_list[1]
  else:
    result = sum(num_list)
  print(result)