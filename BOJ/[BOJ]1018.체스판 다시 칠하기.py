def main():
  result = 64
  for y in range(N-7):
    for x in range(M-7):
      start_w = 0
      start_b = 0
      for m in range(8):
        for n in range(8):
          i = y+m
          j = x+n
          if (i+j) % 2 == 1:
            if arr[i][j] == 'W': start_w += 1
            else : start_b += 1
          else:
            if arr[i][j] == 'B': start_w += 1
            else: start_b += 1
      result = min(start_b,start_w,result)
  print(result)

if __name__ == "__main__":
  N, M = map(int,input().split())
  arr = list(list(input()) for _ in range(N))
  main()