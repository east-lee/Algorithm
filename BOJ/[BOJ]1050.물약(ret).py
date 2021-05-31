def main(potion_name,parent_name_list):
  global min_price

  if potion_name in min_price.keys():
    return min_price[potion_name]

  if potion_name not in market_potion.keys() and potion_name not in recipe_potion.keys():
    return -1
  elif potion_name in market_potion.keys() and potion_name not in recipe_potion.keys():
    return market_potion[potion_name]

  min_potion_price = market_potion[potion_name] if potion_name in market_potion.keys() else 1000000001
  recipes = recipe_potion[potion_name]
  pos = True if potion_name in market_potion.keys() else False


  for recipe in recipes:
    same_name = False
    cant_make = False
    recipe_price = 0
    for sub_potion in recipe:

      sub_potion_cnt, sub_potion_name = int(sub_potion[0]), sub_potion[1:]

      if sub_potion_name in parent_name_list:
        same_name = True
        break
      
      sub_potion_price = main(sub_potion_name,parent_name_list + [sub_potion_name])

      if sub_potion_price == -1:
        cant_make = True
        break


      recipe_price += sub_potion_cnt * sub_potion_price
    if same_name or cant_make: continue
    # print(potion_name,recipe,sub_potion_price)
    min_potion_price = min(min_potion_price,recipe_price)
    pos = True
  # print(min_potion_price,potion_name)

  min_price[potion_name] = min_potion_price if pos else -1

  return min_potion_price if pos else -1


def function_input():
  global market_potion, recipe_potion

  for _ in range(N):
    potion_name, potion_cost = input().split()
    if potion_name in market_potion.keys():
      market_potion[potion_name] = min(market_potion[potion_name], int(potion_cost))
    else: market_potion[potion_name] = int(potion_cost)

  for _ in range(M):
    potion_name, potion_recipe = input().split('=')
    potion_recipe = potion_recipe.split('+')

    if potion_name in recipe_potion.keys():
      recipe_potion[potion_name].append(potion_recipe)
    else:
      new_list = []
      new_list.append(potion_recipe)
      recipe_potion[potion_name]= new_list

if __name__ == "__main__":


  N, M = map(int,input().split())
  market_potion = {}
  recipe_potion = {}
  min_price = {}

  function_input()
  result = main('LOVE',['LOVE'])
  print(result)

