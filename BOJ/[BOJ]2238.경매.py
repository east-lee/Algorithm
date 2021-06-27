def sorting_check_list(arr):

  arr.sort(key = lambda x:len(x))

  return arr

def get_data():
  U,N = map(int,input().split())

  return [U,N]


if __name__ == "__main__":
  U, N = get_data()

  check_list = [
    [] for _ in range(U+1)
  ]

  for _ in range(N):
    name, price = map(str,input().split())
    check_list[int(price)].append(f'{name} {price}')

  check_list = sorting_check_list(check_list)

  for result in check_list:
    if result:
      print(result[0])
      break