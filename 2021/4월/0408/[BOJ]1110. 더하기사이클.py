if __name__ == '__main__':
  N = int(input())

  cnt = 0
  origin_num = str(N)
  new_num = -1
  if N == 0:
    print(1)
  else:
    while True:
      cnt += 1
      if len(origin_num)<2: origin_num = '0'+origin_num
      check_num = str(int(origin_num[0])+int(origin_num[1]))
      new_num = origin_num[1] + check_num[-1]
      if int(new_num) == N:
        break
      origin_num = new_num
    print(cnt)
