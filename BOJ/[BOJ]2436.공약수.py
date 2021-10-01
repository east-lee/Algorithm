
def GCD(num_a, num_b):

  while num_b:
    mod = num_b
    num_b = num_a % num_b
    num_a = mod
  return num_a

if __name__ == "__main__":
  A, B = map(int, input().split())
  div = B//A
  a, b = 1, div
  for i in range(1, div//2 + 1):
    if not div % i:
      c = i
      d = div//i
      if GCD(c,d) != 1:
        continue
      if a + b > c + d:
        a = c
        b = d
  print(a*A, b*A)

