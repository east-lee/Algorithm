def get_data():
  string_data = list(input())
  return string_data


def solution(length):
  global arr
  arr.append(''.join(data[length:]))

if __name__ == "__main__":
  data = get_data()
  arr = []

  for i in range(len(data)):
    solution(i)

  arr.sort()

  for a in arr: print(a)
