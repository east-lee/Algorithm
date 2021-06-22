
def contest(ranking, year):
  price_num_17 = [i for i in range(1,7)]
  price_17 = [500, 300, 200, 50, 30, 10]

  price_num_18 = [1, 2, 4, 8, 16]
  price_18 = [512, 256, 128, 64, 32]

  max_ranking = 21 if year == 2017 else 31

  if ranking > max_ranking or not ranking:
    return 0
  total_ranking = 0
  for i in range(6):
    num = price_num_17[i] if year == 2017 else price_num_18[i]
    if total_ranking < ranking <= total_ranking + num:
      return price_17[i] if year == 2017 else price_18[i]
    total_ranking += num



if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    a, b = map(int,input().split())
    total_price = contest(a, 2017) + contest(b, 2018)
    print(total_price*10000)