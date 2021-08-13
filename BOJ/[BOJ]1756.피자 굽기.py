def get_data():
  D, N = map(int, input().split())
  OVEN, PIZZA = [list(map(int, input().split()))
                 for _ in range(2)]

  return [D, N, OVEN, PIZZA]

if __name__ == "__main__":

  D, N, OVEN, PIZZA = get_data()

  for i in range(1, D):
    OVEN[i] = min(OVEN[i - 1], OVEN[i])

  pizza_idx, result = 0, D-1
  print_result = 0
  for i in range(D-1, -1, -1):

    if pizza_idx >= N:
      print_result = result + 1
      break

    if OVEN[i] >= PIZZA[pizza_idx]:
      pizza_idx += 1
      result = i

  print(print_result)