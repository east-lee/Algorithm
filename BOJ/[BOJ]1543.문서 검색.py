
if __name__ == "__main__":
  STRING = [
    list(input()) for _ in range(2)
  ]

  start_idx = 0
  result = 0

  while start_idx + len(STRING[1]) <= len(STRING[0]):
    if STRING[0][start_idx:start_idx + len(STRING[1])] == STRING[1]:
      result += 1
      start_idx += len(STRING[1])
    else:
      start_idx += 1

  print(result)