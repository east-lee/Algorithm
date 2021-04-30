def main():
  for i in range(3,n+1//2 +1):
    x = i
    y = n-i

    if x%2 and y%2 and prime[x] + prime[y] == 0:
      return f'{n} = {x} + {y}'
  return "Goldbach's conjecture is wrong."

def find_prime():
  arr = [0] * 1000001
  arr[1] = 1
  for i in range(2,1000001):
    if arr[i] == 0:
      x = 2*i
      while x <= 1000000:
        arr[x] = 1
        x += i
  return arr

if __name__ == "__main__":
  prime= find_prime()
  while True:
    n = int(input())
    if not n: break
    print(main())