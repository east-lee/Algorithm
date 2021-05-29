def main():
  start_num = 665
  cnt = 0
  while cnt < N:
    start_num += 1
    if '666' in str(start_num):
      cnt += 1
  print(start_num)

if __name__ == '__main__':
  N = int(input())
  main()