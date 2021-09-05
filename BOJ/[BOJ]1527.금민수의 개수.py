def find_num(k=0, check_num=0):
  global result

  if check_num > B: return;
  elif check_num >= A:
    result += 1

  find_num(k + 1, int(str(check_num) + "4"))
  find_num(k + 1, int(str(check_num) + "7"))


def get_data():
  A, B = map(int, input().split())

  return [A, B]


if __name__ == "__main__":
  A, B = get_data()
  result = 0
  find_num()

  print(result)
