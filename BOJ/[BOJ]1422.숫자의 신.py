# 난이도 플래티넘5

from functools import cmp_to_key

def check_size(a,b):
  A, B = int(a+b), int(b+a)

  if A > B: return -1
  return 1


def main():
  global number_list, result

  max_repeat = N - K
  max_num = number_list[0]

  for _ in range(max_repeat):
    number_list.append(max_num)

  number_list = sorted(number_list,key=cmp_to_key(lambda a,b : check_size(a,b)))

  result = ''.join(number_list)

def get_data():
  K, N = map(int,input().split()) # 0< K <= N <= 1000
  number_list = []

  for _ in range(K):
    input_num = int(input())
    number_list.append(input_num)

  number_list.sort(key=lambda x:-x)

  return [K, N, number_list]

if __name__ == "__main__":
  K, N, number_list = get_data()
  number_list = list(map(str,number_list))
  result = ''
  main()
  print(result)


# def check_size(a,b):
#   if int(a+b) > int(b+a):
#     return a+b
#   return b+a

# def main():
#   global result, number_list
#
#   max_num_repeat_cnt = N-K
#   max_num = number_list[0]
#
#   # 초기 세팅
#   result = max_num * (max_num_repeat_cnt)
#
#   for i in range(K):
#     if result:
#       result = check_size(result,number_list[i])
#     else:
#       result += number_list[i]
