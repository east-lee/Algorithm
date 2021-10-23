if __name__ == "__main__":
  tc = 0
  while True:
    tc += 1
    input_data = list(input())
    if "-" in input_data: break
    cnt = 0
    stack = []

    for chr in input_data:
      if chr == "{":
        stack.append(chr)
      elif not stack:
        cnt += 1
        stack.append("{")
      else:
        stack.pop()

    cnt += len(stack)//2

    print(f'{tc}. {cnt}')