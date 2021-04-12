if __name__ == "__main__":
  n = int(input())
  arr = []
  for _ in range(n):arr.append(int(input()))

  stack = []
  result = 'NO'
  result_arr = []
  for i in range(1,n+1):
    stack.append(i)
    result_arr.append('+')
    while True:
      if stack and stack[-1] == arr[0]:
        result_arr.append('-')
        stack.pop()
        arr = arr[1:]
      else:
        break
  if not arr:
    for i in result_arr:print(i)
  else:
    print('NO')