def find_prime_num():
  n = int(B**0.5) + 1
  prime_list = []
  prime_check = [False] * n

  for i in range(2, n):
    if not prime_check[i]:
      prime_list.append(i)
      x = 2*i
      while x < n:
        prime_check[x] = True
        x += i
  return prime_list

if __name__ == "__main__":
  A, B = map(int ,input().split())
  prime_list = find_prime_num()
  result = 0
  for prime in prime_list:
    x = prime ** 2
    while x <= B:
      if x >= A: result += 1
      x *= prime
  print(result)