def find_prime():
  max_num = 10**6

  prime_check = [False] * max_num
  prime = []

  for i in range(2, max_num):
    if prime_check[i]: continue

    x = i + i
    prime.append(i)

    while x < max_num:
      prime_check[x] = True
      x += i

  return prime





if __name__ == "__main__":
  N = int(input())
  prime = find_prime()

  for _ in range(N):
    S = int(input())
    check = True

    for p in prime:
      if not S % p:
        check = False
        break

    print("YES") if check else print("NO")
