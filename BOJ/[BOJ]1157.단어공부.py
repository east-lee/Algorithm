if __name__ == "__main__":
  arr = input()
  check_dict = {}

  for i in arr:
    if i.upper() in check_dict:
      check_dict[i.upper()] += 1
    else:
      check_dict[i.upper()]= 1

  check = sorted(check_dict.items(),key=(lambda x:x[1]),reverse=True)

  if len(check) > 1 and check[0][1] == check[1][1]:
    print('?')
  else:
    print(check[0][0])
