def main():
  global good_num_list
  cnt = 0
  for i in range(2,N):
    for j in range(i):
      result_num = num_list[i]
      if result_num in good_num_list:
        break
      if str(result_num-num_list[j]) in num_list_dict.keys() and num_list_dict[str(result_num-num_list[j])] != j  and num_list_dict[str(result_num-num_list[j])] != i:
        good_num_list.append(result_num)
        cnt += num_list.count(result_num)
        break
  print(cnt)


if __name__ == "__main__":
  N = int(input())
  num_list = list(map(int,input().split()))
  num_list.sort()
  num_list_dict = {}
  good_num_list = []
  cnt = 0
  for num in num_list:
    num_list_dict[str(num)] = cnt
    cnt += 1

  main()


