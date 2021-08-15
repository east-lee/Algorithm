def get_data():
  M, N = map(int, input().split())
  apartment = [
    list(input()) for _ in range(4*M+M+1)
  ]

  return [M, N, apartment]

if __name__ == "__main__":
  M, N, apartment = get_data()

  row_cnt, col_cnt = 0, 0
  result = [0 for _ in range(5)]


  while col_cnt < M:
    find_x = 1
    row_cnt = 0
    while row_cnt < N:
      find_y = (col_cnt * 5) + 1
      cnt = 0
      while apartment[find_y][find_x] == '*':
        cnt += 1
        find_y += 1
      result[cnt] += 1
      row_cnt += 1
      find_x += 5
    col_cnt += 1

  print(" ".join(list(map(str,result))))

