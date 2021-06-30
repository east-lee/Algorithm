def main():
  min_cost, max_money = egg_cost[0]+1, 0
  max_range = min(N,M)
  for index in range(max_range):
    cnt = index + 1
    if max_money < cnt * egg_cost[index]:
      max_money = cnt * egg_cost[index]
      min_cost = egg_cost[index]

  return [min_cost, max_money]


def get_data():
  N, M = map(int,input().split())
  egg_cost = [int(input()) for _ in range(M)]
  egg_cost.sort(reverse=True)

  return [N,M,egg_cost]



if __name__ == "__main__":
  N, M, egg_cost = get_data()

  min_cost, max_money = main()

  print(min_cost,max_money)