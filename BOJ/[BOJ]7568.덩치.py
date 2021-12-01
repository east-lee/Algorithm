def get_data():
  N = int(input())
  data_list = []

  for _ in range(N):
    x, y = map(int, input().split())
    data_list.append([x,y])

  return [N, data_list]


if __name__ == "__main__":
  N, data_list = get_data()
  result = [0]* N

  for i in range(N-1):
    for j in range(i+1, N):
      x1, y1 = data_list[i]
      x2, y2 = data_list[j]

      if x1 < x2 and y1 < y2:
        result[i] += 1
      elif x1 > x2 and y1 > y2:
        result[j] += 1

  for r in result:
    print(r+1, end= " ")
  print()