def find_num_to_Z():
  global K, num_to_Z_list
  cnt = max_data_length - 1
  while cnt >=0 and K:
    check_dict = data_check_dict[cnt]
    check_dict = sorted(check_dict.items(),key=lambda x:(x[1],-ord(x[0])),reverse=True)

    for key,key_cnt in check_dict:
      if key == 'Z': continue
      if key in num_to_Z_list: continue
      else:
        num_to_Z_list.append(key)
        K -= 1

      if not K: break
    cnt -= 1

def try_except(num):
  try:
    num = int(num)
    return num
  except:
    num = ord(num) - 55
    return num

def change_32_to_10(str_num):
  num = 0
  for i in range(len(str_num)):
    x = 32 ** (i)
    y = try_except(str_num[i])
    num += x*y
  return num

def change_num_to_z():
  total_sum = 0

  for data in data_list:
    new_data = ''
    for word in data:
      if word in num_to_Z_list:
        new_data += 'Z'
      else: new_data += word
    print(data, change_32_to_10(new_data))
    total_sum += change_32_to_10(new_data)
  # print(num_to_Z_list)
  # print(total_sum)
  # print(total_sum%32)




if __name__ == "__main__":
  N = int(input())
  data_list = []
  data_check_dict = [{} for _ in range(50)] #최대 길이 50이니까
  max_data_length = 0
  num_to_Z_list = []

  for _ in range(N):
    input_data = list(input())[::-1]
    data_list.append(input_data)
    max_data_length = max(max_data_length,len(input_data))

    for i in range(len(input_data)):
      if input_data[i] in data_check_dict[i].keys():
        data_check_dict[i][input_data[i]] += 1
      else: data_check_dict[i][input_data[i]] = 1

  data_check_dict = data_check_dict[:max_data_length]

  K = int(input())
  find_num_to_Z() #자릿수가 높고 많이 등장한거부터 Z로 변환한다, 다 동일하다면 가장 낮은 수부터 변환하도록 한다.
  print(num_to_Z_list)
  result = change_num_to_z() #위에서 구한 변한 수로 값들을 실제로 변환한다




















# 숫자를 거꾸로생각 ... ㅎㅎ
# def change_num_to_Z():
#   global data_list
#   new_list = []
#   for data in data_list:
#     new_data = ''
#     for word in data:
#       if word in num_to_Z_list:
#         new_data+='Z'
#       else:
#         new_data += word
#     new_list.append(new_data)
#   return new_list
#
#
# def change_to_num(n):
#   try:
#     n = int(n)
#     return n
#   except:
#     return ord(n) - 55
#
# def sum_32():
#   data_list = change_num_to_Z()
#   total_sum = 0
#
#   for data in data_list:
#     check_sum = 0
#     for i in range(len(data)):
#
#
#
#
#       check_sum += (32**(len(data)-i-1))*change_to_num(i)
#     total_sum += check_sum
#   return total_sum
#
#
#
#
#
# def main():
#   global K,num_to_Z_list
#   cnt = data_max_length - 1
#   while cnt >= 0 and K > 0:
#     check_dict = data_length_dict[cnt]
#     check_dict = sorted(check_dict.items(),key=lambda x:(x[1],-ord(x[0])), reverse=True)
#
#     for key, key_cnt in check_dict:
#       if key in num_to_Z_list:
#         continue
#       else:
#         num_to_Z_list.append(key)
#         K-=1
#       if K == 0: break
#     cnt -= 1
#
#   return sum_32()
#
# if __name__ == "__main__":
#
#   N = int(input())
#
#   data_length_dict = [{} for _ in range(50)]
#   data_list = []
#   data_max_length = 0
#   num_to_Z_list = []
#
#   for _ in range(N):
#     input_data = list(input())
#     data_list.append(input_data)
#     data_max_length = max(data_max_length,len(input_data))
#     input_data = input_data[::-1]
#     for i in range(len(input_data)-1,-1,-1):
#       if input_data[i] in data_length_dict[i].keys():
#         data_length_dict[i][input_data[i]] += 1
#       else: data_length_dict[i][input_data[i]] = 1
#
#
#   K = int(input())
#   data_length_dict = data_length_dict[:data_max_length]
#
#   result = (main())
#   print(result)
#   print_result = ''
#   while result:
#     print_result += str(result % (32))
#     print(str(result % (32)))
#     result = result//(32)
#
#   print(print_result)
