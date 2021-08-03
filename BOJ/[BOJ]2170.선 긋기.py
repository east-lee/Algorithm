def get_data():
  N = int(input())

  line_list = [
    list(map(int,input().split())) for _ in range(N)
  ]

  line_list.sort(key = lambda x:x[0])

  return [N, line_list]


if __name__ == "__main__":
  N, line_list = get_data()
  result = 0

  cnt = 1
  left, right = line_list[0]

  while cnt < N:
    x, y = line_list[cnt]

    if right < x: # 연결이 끊겨있을 경우
      result += abs(left - right)
      left, right = x, y
    elif right == x:
      right = y
    elif right > x:
      if right < y:
        right = y
    cnt += 1
  result += abs(left-right)

  print(result)
