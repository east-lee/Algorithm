def main(num):
  result = 0
  for i in range(num+1,2*num+1):
    if prime_list[i] == 0:
      result += 1

  print(result)

def get_prime():
  check_list = [0] * (max_2n + 1)
  check_list[0] = 1
  check_list[1] = 1

  for i in range(2,max_2n + 1):
    if check_list[i] == 0:
      num = i + i
      while num <= max_2n:
        check_list[num] = 1
        num += i

  return check_list

def get_n():
  n_list = []

  while True:
    n = int(input())
    if not n: break
    n_list.append(n)

  return n_list

if __name__ == "__main__":
  n_list = get_n()
  max_2n = max(n_list)*2

  prime_list = get_prime()

  for num in n_list:
    main(num)