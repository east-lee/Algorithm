if __name__ == "__main__":
  N = int(input())

  i, result = 2, 1

  while i**2 <= N:
    if not N % i:
      result = N//i
      break
    i += 1

  print(N-result)