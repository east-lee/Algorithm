def main():
  M = int(input())

  for _ in range(M):
    check = list(input())

    keyword = check[0]+check[-1]
    if len(check) <= 2 and ''.join(check) in len_2_check:
      print(1)
      continue
    elif len(check) <=2:
      print(0)
      continue

    check = check[1:-1]
    check.sort()
    check = ''.join(check)

    if keyword in dictionary.keys() and check in dictionary[keyword].keys():
      print(dictionary[keyword][check])
    else:print(0)

if __name__ == "__main__":
  N = int(input())
  dictionary = {}
  len_2_check = []
  for _ in range(N):
    check = list(input())
    if len(check) <= 2:
      len_2_check.append(''.join(check))
      continue
    keyword = check[0]+check[-1]
    check = check[1:-1]
    check.sort()
    check = ''.join(check)
    if keyword not in dictionary.keys(): dictionary[keyword] = {}
    if check == '':
      dictionary[keyword]['null'] = 1
    elif check not in dictionary[keyword].keys():
      dictionary[keyword][check] = 1
    else: dictionary[keyword][check] += 1

  main()

