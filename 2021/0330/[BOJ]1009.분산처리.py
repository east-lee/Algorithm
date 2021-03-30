def main():
  v = [0]*10
  check_list = []
  check = a
  while True:
    if v[check]:
      break

    v[check] = 1
    check_list.append(check)

    check *= a
    check %= 10

  print(check_list[b%len(check_list)-1])

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    a, b = map(int,input().split())
    main()