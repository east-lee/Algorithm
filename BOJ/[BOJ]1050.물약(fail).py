import sys

def main(potion_name):
  if potion_name not in make_potion.keys() and potion_name not in market.keys():
    return -1

  if potion_name in market.keys():
    return market[potion_name]

  recipes = make_potion[potion_name]
  recipe_min_price = sys.maxsize

  for recipe in recipes:
    recipe_price = 0
    breaker = False
    print(recipe,potion_name)
    for sub_potion in recipe:
      num = int(sub_potion[0])
      name = sub_potion[1:]
      if potion_name==name:
        breaker = True
        break
      min_potion_price = main(name)
      if min_potion_price == -1:
        return -1
      else:
        recipe_price += num * min_potion_price
    print(recipe_price,potion_name)
    if breaker: break
    if recipe_min_price == sys.maxsize and recipe_price == -1:
      recipe_min_price = -1
    elif (recipe_min_price == sys.maxsize or recipe_min_price == -1) and recipe_price != -1:
      recipe_min_price = recipe_price
    elif recipe_min_price != -1 and recipe_price != -1:
      recipe_min_price = min(recipe_min_price,recipe_price)
  print(recipe_min_price)
  return recipe_min_price

if __name__ == "__main__":
  N, M = map(int,input().split())
  market = {}
  make_potion = {}

  for _ in range(N):
    potion_name, potion_price = input().split()
    if potion_name in market.keys():
      market[potion_name] = min(market[potion_name],int(potion_price))
    else: market[potion_name] = int(potion_price)

  for _ in range(M):
    making_potion_name, sub_potion_list = input().split('=')
    sub_potion_list = sub_potion_list.split('+')
    if making_potion_name in make_potion.keys():
      make_potion[making_potion_name].append(sub_potion_list)
    else:
      sub_list = []
      sub_list.append(sub_potion_list)
      make_potion[making_potion_name] = sub_list

  result = main('LOVE')

  print(result) if result <= 1000000000 else print(1000000001)