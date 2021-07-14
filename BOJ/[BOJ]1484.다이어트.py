def main():
  result = []
  left, right = 0,0

  while left < 100000 and right < 100000:
    check_result = (X[left] + MEMORY[right]) * (X[left] - MEMORY[right])

    if check_result == G:
      result.append(X[left])
      right += 1
    elif check_result < G:
      left += 1
    else: right += 1

  return result if result else -1

if __name__ == "__main__":
  G = int(input())
  # G = X**2 - MEMORY**2 = (X+MEMORY)(X-MEMORY)
  X, MEMORY = [[i for i in range(1,100001)] for _ in range(2)]
  result = main()

  if result == -1 : print(result)
  else:
    for r in result: print(r)
