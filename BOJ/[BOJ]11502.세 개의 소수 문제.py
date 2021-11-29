

def get_prime():
  prime_check = [False] * (max_num+1)
  prime = []
  prime_check[0], prime_check[1] = True, True

  for i in range(2, max_num+1):
    if prime_check[i] == False:
      x = i*2
      prime.append(i)
      while x <= max_num:
        prime_check[x] = True
        x += i

  return [prime_check, prime]

def get_data():
  TC = int(input())
  arr = list(int(input()) for _ in range(TC))

  return [TC, arr]

def dfs(num, k=0, sum_num = 0, last_idx = 0, temp = []):
  global result
  if k == 2:
    mod_num = num - sum_num
    if prime_check[mod_num] == False:
      result = temp + [mod_num]
    return

  for i in range(len(prime)):
    if prime[i] >= num:
      break

    dfs(num, k+1, sum_num + prime[i], i, temp + [prime[i]])

    if result != 0:
      return

def solution(num):
  dfs(num)


if __name__ == "__main__":
  TC, arr =get_data()
  max_num = max(arr)
  prime_check, prime = get_prime()
  result = 0
  for num in arr:
    result = 0
    solution(num)

    if result == 0:
      print(0)
    else:
      for x in result:
        print(x, end = " ")
      print()