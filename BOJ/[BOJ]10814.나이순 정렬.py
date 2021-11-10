def get_data():
  N = int(input())
  arr = []

  for _ in range(N):
    age, name = map(str, input().split())
    arr.append([int(age), name])

  return arr


if __name__ == "__main__":
  arr = get_data()
  arr.sort(key = lambda x:int(x[0]))

  for age, name in arr:
    print(age, name)