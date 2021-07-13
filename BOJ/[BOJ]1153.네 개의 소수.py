def main(n):
  for num in prime:
    mod_num = n - num
    if check_num[mod_num] == False:
      return str(num) + ' ' + str(mod_num)


def get_prime():
  check_num = [False] * (N+1)
  check_num[0], check_num[1] = [True for _ in range(2)]
  prime = []
  for x in range(2,N+1):
    if check_num[x] == False:
      num = x * 2
      prime.append(x)
      while num <= N:
        check_num[num] = True
        num += x
  return [check_num,prime]


if __name__ == "__main__":
  N = int(input())
  check_num, prime = get_prime()
  mid_result = False

  if N < 8: print(-1)
  else:
    result = ''
    if N % 2 == 0: #짝수일경우
      result = '2 2 ' + main(N-4)
    else:
      result = '2 3 ' + main(N-5)
    print(result)