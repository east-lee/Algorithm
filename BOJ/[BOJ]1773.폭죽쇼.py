def main():
  time = [0] * (C+1)

  for bomb in bomb_cycle:
    check_time = bomb
    while check_time <= C:
      time[check_time] = 1
      check_time += bomb

  return time.count(1)


def get_data():
  N, C = map(int,input().split())
  bomb_cycle = []

  for _ in range(N):
    bomb_cycle.append(int(input()))

  return [N,C,bomb_cycle]


if __name__ == "__main__":
  N, C, bomb_cycle = get_data()
  print(main())