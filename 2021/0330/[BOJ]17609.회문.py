def main(string):
  if string == string[::-1]:
    print(0)
    return
  last_idx = len(string)-1
  start_idx = 0
  skip_cnt = 0
  result = 0
  while last_idx>=start_idx:
    if string[start_idx] == string[last_idx]:
      last_idx -= 1
      start_idx += 1
    else:
      if skip_cnt:
        result =2
        break
      else:
        if string[start_idx] == string[last_idx-1]:
          start_idx += 1
          last_idx -= 2
        elif string[start_idx + 1] == string[last_idx]:
          start_idx += 2
          last_idx -= 1
        skip_cnt = True

  if not result:
    if skip_cnt: result = 1
    else: result = 0
  print(result)


if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    input_str = input()
    main(input_str)