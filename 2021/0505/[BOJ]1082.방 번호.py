def main():
  global money

  min_cost = min(cost)
  min_cost_num = list(str(cost.index(min_cost))*(money//min_cost))
  money -= (money//min_cost) * min_cost

  for i in range(len(min_cost_num)):
    return_money = cost[0]
    money += return_money
    for j in range(N-1,cost.index(min_cost)-1,-1):
      if cost[j] <= money:
        money -= cost[j]
        min_cost_num[i] = str(j)
        break

  result = int(''.join(min_cost_num))
  if result == 0:
    while len(min_cost_num) > 0:
      min_cost_num = min_cost_num[1:]
      money += cost[0]
      for j in range(N-1,0,-1):
        if cost[j] <= money:
          min_cost_num.insert(0,str(j))
          break
      if min_cost_num[0] != '0': break
  result = int(''.join(min_cost_num))

  return result


if __name__ == "__main__":
  N = int(input())
  cost = list(map(int,input().split()))
  money = int(input())
  print(main())