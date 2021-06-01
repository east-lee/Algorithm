def main():
  num_list = [S//K] * K
  num_mod = S % K
  cnt = 0
  while num_mod:
    num_list[cnt] += 1
    num_mod -= 1
    cnt += 1

  result = 1
  for i in num_list:
    result *= i
  print(result)

if __name__ == "__main__":
  S, K = map(int,input().split())
  main()