def prime():
  check = [True]*1000001
  check[0],check[1] = False,False
  for i in range(2,1000001):
    if check[i] == True:
      x = i+i
      while x<1000001:
        check[x] = False
        x += i
  return check
if __name__ == "__main__":
  T = int(input())
  check = prime()
  for _ in range(T):
    N = int(input())
    x = 1
    result = 0
    while x<=N//2+1:
      x += 1
      y = N-x
      if x<=y and check[y] and check[x]:
        result += 1
    print(result)
