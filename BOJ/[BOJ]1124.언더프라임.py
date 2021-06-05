def main(num):
  cnt = 0
  idx = 0
  while num != 1 and idx < len(prime):
    prime_num = prime[idx]
    while True:
      if prime_num <= num and num % prime_num == 0:
        num = num//prime_num
        cnt += 1
      else:
        break
    idx += 1
  if num == 1 and check_list[cnt]==0:
    return 1
  return 0

def find_prime():
  num_list = [0]*(B+1)
  num_list[0],num_list[1] = 1, 1
  prime_list = []
  for i in range(2,B+1):
    if num_list[i] == 1:
      continue
    num = 2*i
    prime_list.append(i)
    while num <= B:
      num_list[num] = 1
      num += i
  return [num_list,prime_list]

if __name__ == "__main__":
  A, B = map(int,input().split())
  check_list, prime = find_prime()
  result = 0
  for num in range(A,B+1):
    result += main(num)
  print(result)
