

def get_data():
  M, N = map(int, input().split())

  grow_info = [
    0 for _ in range(2*M-1)
  ]

  for _ in range(N):
    info = list(map(int, input().split()))
    idx = 0
    for i in range(3):
      cnt = 0
      while cnt < info[i]:
        grow_info[idx] += i
        idx += 1
        cnt += 1

  return [M, N, grow_info]


if __name__ == "__main__":
  M, N, get_info = get_data()

  arr = [
    [1] * M for _ in range(M)
  ]

  check = [[0] * M for _ in range(M)]

  cnt, i, j = 0, M-1, 0
  direction = [-1, 0]

  while cnt < len(get_info):
    check[i][j] = get_info[cnt]
    arr[i][j] += get_info[cnt]
    cnt += 1
    i, j = i + direction[0], j + direction[1]

    if i < 0:
      i, j = 0, 1
      direction = [0, 1]

  for i in range(1, M):
    for j in range(1, M):
      max_grow = max([check[i-1][j], check[i][j-1], check[i-1][j-1]])
      check[i][j] = max_grow
      arr[i][j] = max_grow + 1

  for line in arr:
    line = list(map(str,line))
    print(" ".join(line))