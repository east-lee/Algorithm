if __name__ == "__main__":
  N, K = map(int,input().split())
  roulette = ['?']*N
  result = ''
  arrow_index = 0
  for _ in range(K):
    plus_index, string = map(str,input().split())
    arrow_index += int(plus_index)
    if arrow_index >= N: arrow_index = arrow_index % N
    if roulette[arrow_index] != '?' and roulette[arrow_index] != string:
      result = '!'
    roulette[arrow_index] = string
    if roulette.count(string) >= 2: result = '!'

  if result == '!': print(result)
  else:
    cnt = 0
    while cnt < N:
      if arrow_index == -1: arrow_index = N-1
      result += roulette[arrow_index]
      cnt += 1
      arrow_index -= 1
    print(result)