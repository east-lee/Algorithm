if __name__ == "__main__":
  N = int(input())
  result = 0

  while N >=5:
    result += N//5
    N = N//5

  print(result)