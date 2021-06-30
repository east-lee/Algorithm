for _ in range(3):
  N = int(input())
  sum_result = 0

  for _ in range(N):
    sum_result += int(input())

  if sum_result < 0: print('-')
  elif sum_result == 0: print('0')
  else: print('+')
