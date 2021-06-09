def case_1(money):
  return money * 0.78

def case_2(money):
  return money * 0.8 + money * 0.2 * 0.78

def main():
  contest_winner_money = int(input())

  case_1_money = int(case_1(contest_winner_money))
  case_2_money = int(case_2(contest_winner_money))

  print(case_1_money, case_2_money)

if __name__ == "__main__":
  main()