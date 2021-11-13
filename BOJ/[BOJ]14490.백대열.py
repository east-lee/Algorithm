def get_data():
  A, B = map(int, input().split(":"))
  # print(A, B)
  return [A, B]

def solution():
  data = [A, B]
  data.sort(key=lambda x:x)
  x, y = data

  while y:
    temp = x
    x = y
    y = temp%y
  return x

if __name__ == "__main__":
  A, B = get_data()
  g = solution()
  print(f'{A//g}:{B//g}')