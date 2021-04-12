if __name__ == "__main__":
  N,M = map(int,input().split())
  check_list = list(map(int,input().split()))
  arr = list(i for i in range(1,N+1))
  result = 0
  while check_list:
    # 현재배열의 첫번째값과 check_list의 첫번째값이 동일하다면 제거
    if arr[0] == check_list[0]:
      check_list = check_list[1:]
      arr = arr[1:]
    else:
      # 다음으로 제거되어야할 숫자의 인덱스를 확인
      remove_num_idx = arr.index(check_list[0])
      # 해당인덱스가 맨앞으로 오기위한 각각의 최소의 경우를 구한다.
      left_cnt = remove_num_idx
      right_cnt = len(arr)-remove_num_idx
      arr = arr[remove_num_idx:] + arr[:remove_num_idx]
      result += min(left_cnt,right_cnt)
  print(result)