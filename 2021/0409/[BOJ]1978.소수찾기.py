def searchPrime():
  check = [False for _ in range(1001)]
  check[0],check[1] = True, True
  for i in range(2,1001):
    if check[i] == False:
      x = 2*i
      while x<=1000:
        check[x] = True
        x += i
  return check

if __name__ == "__main__":
  N = int(input())
  arr = list(map(int,input().split()))
  prime_list = searchPrime()
  result = 0
  for i in arr:
    if prime_list[i] == False: result += 1
  print(result)