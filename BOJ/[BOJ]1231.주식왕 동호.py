def find_max_stock(money, day):
  max_money = money

  for n in range(C):
    now_price, tomorrow_price = stock[n][day - 1], stock[n][day]
    if now_price > money: continue
    # 남은 돈으로도 살수있는 주식이 있는지 체크
    tomorrow_money = (money // now_price) * tomorrow_price + (find_max_stock(money % now_price,day))
    max_money = max(max_money, tomorrow_money)

  return max_money


def main():
  dp = [0] * (D + 1)
  dp[0] = M  # 첫날 가지고 있는 돈은 M원

  for day in range(1, D):
    dp[day] = find_max_stock(dp[day - 1], day)

  print(dp[D - 1])


if __name__ == "__main__":
  C, D, M = map(int, input().split())
  stock = list(list(map(int, input().split())) for _ in range(C))
  main()
