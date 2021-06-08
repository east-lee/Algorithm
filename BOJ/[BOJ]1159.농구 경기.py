if __name__ == "__main__":
  N = int(input())
  check_dict = {}

  for _ in range(N):
    first_name = input()[0]
    if first_name in check_dict.keys():
      check_dict[first_name] += 1
    else: check_dict[first_name] = 1

  check_dict = sorted(check_dict.items(),key=lambda x:(x[0]))

  result = ''

  for first_name, cnt in check_dict:
    if cnt >= 5:
      result += first_name

  if result: print(result)
  else: print('PREDAJA')