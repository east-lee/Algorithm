if __name__ == "__main__":
  N,K = map(int,input().split())
  num = input()
  remove_check = list(0 for _ in range(10))
  num_cnt = list(0 for _ in range(10))

  for i in num:
    num_cnt[int(i)] += 1

  cnt = 0
  while K:
    if K <= num_cnt[cnt]:
      remove_check[cnt] += K
      K = 0
    else:
      K -= num_cnt[cnt]
      remove_check[cnt] += num_cnt[cnt]
    cnt += 1

  result = ''

  for i in num:
    if remove_check[int(i)]:
      remove_check[int(i)] -= 1
    else:
      result += i
  print(int(result))


