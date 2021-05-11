def main():
  button_time = [300,60,10]

  t = int(time)
  cnt = 0
  idx = 0
  while idx < 3:
    print(t//button_time[idx],end=' ')
    t = (t%button_time[idx])
    idx += 1

  print()

if __name__ == "__main__":
  time = input()
  if list(time)[-1] != '0':
    print(-1)
  else: main()