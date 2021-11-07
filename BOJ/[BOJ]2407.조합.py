import math

def solution():
  x = math.factorial(A)
  y = math.factorial(A-B) * math.factorial(B)

  return x//y

if __name__ == "__main__":
  A, B = map(int, input().split())

  print(solution())