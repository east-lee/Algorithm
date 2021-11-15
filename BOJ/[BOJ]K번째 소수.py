def get_prime():
  max_size = K * 30
  prime_check = [False] * max_size
  prime_check[0], prime_check[1] = True, True
  prime = []

  for i in range(2, max_size):
    if prime_check[i] == False:
      x = i*2
      prime.append(i)

      while x < max_size:
        prime_check[x] = True
        x += i

  return prime

if __name__ == "__main__":
  K = int(input())
  prime = get_prime()
  print(prime[K-1])

