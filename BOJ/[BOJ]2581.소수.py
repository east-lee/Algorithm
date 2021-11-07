def get_prime():
  max_num = 10001
  prime_list = []
  prime_check = [False] * max_num
  prime_check[0], prime_check[1] = True, True

  for i in range(2, max_num):
    if prime_check[i]: continue

    prime_list.append(i)
    x = i * 2

    while x < max_num:
      prime_check[x] = True
      x += i

  return prime_list

if __name__ == "__main__":
  prime_list = get_prime()

  M, N = [int(input()) for _ in range(2)]
  result = [0,0]

  for prime_num in prime_list:
    if prime_num < M: continue
    elif prime_num > N: break
    if result[0] == 0:
      result[0] = prime_num
    result[1] += prime_num

  if result[1] == 0:
    print(-1)
  else:
    print(result[1])
    print(result[0])