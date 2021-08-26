if __name__ == "__main__":
  S = list(input())
  stack = []
  result = 0

  for s in S:
    # print(stack)
    if s != ")":
      try:
        s = int(s)
        stack.append(str(s) + "num")
      except:
        stack.append(s)
    else:
      length = 0

      while True:
        check_s = stack.pop()
        if check_s == "(":
          break
        else:
          try:
            length += int(check_s)
          except:
            length += 1
      length = int(stack.pop()[:1]) * length
      stack.append(length)
  # print(stack)
  for s in stack:
    # print(s,"s!!")
    try:
      s = int(s)
      result += s
    except:
      result += 1

  print(result)