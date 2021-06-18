def main_1():
  sum_array = sum(num_array)
  int_sum_array = sum_array // N
  result_main_1 = sum_array / N

  if int_sum_array + 0.5 <= result_main_1:
    print(int_sum_array+1)
  else: print(int_sum_array)

  main_2()

def main_2():
  mid_index = N//2
  print(num_array[mid_index])
  main_3()

def main_3():
  checked = [0]*8002
  max_cnt = 0
  max_list = []


  for idx in range(N):
    check_num = num_array[idx]
    if checked[check_num+4000] == 1: continue
    checked[check_num+4000] = 1
    cnt = 0
    for jdx in range(idx,N):
      if num_array[jdx] == check_num:
        cnt += 1
      else: break
    if max_cnt < cnt:
      max_cnt = cnt
      max_list = [check_num]
    elif max_cnt == cnt:
      max_list.append(check_num)

  if len(max_list) >= 2:
    max_list.sort()
    print(max_list[1])
  else: print(max_list[0])
  main_4()

def main_4():
  print(num_array[-1]-num_array[0])



if __name__ == "__main__":
  N = int(input())
  num_array = []
  for _ in range(N):
    num_array.append(int(input()))
  num_array.sort()
  main_1()