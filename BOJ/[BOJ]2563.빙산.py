def count_sea_side(point):
  i, j = point
  cnt = 0

  for k in range(4):
    ny, nx = i + direction[k][0], j + direction[k][1]
    if 0<=ny<N and 0<=nx<M and iceberg[ny][nx] == 0:
      cnt += 1

  return cnt

def melt_iceberg():
  iceberg_point_list = []

  next_iceberg = [
    [0] * M for _ in range(N)
  ]

  for i in range(N):
    for j in range(M):
      if iceberg[i][j]:
        iceberg_point_list.append([i,j])

  if len(iceberg_point_list) == 0:
    return False

  for iceberg_point in iceberg_point_list:
    i, j = iceberg_point
    next_iceberg[i][j] = max(iceberg[i][j] - count_sea_side(iceberg_point), 0)

  return next_iceberg



def count_iceberg():
  visited = [
    [False] * M for _ in range(N)
  ]

  iceberg_cnt = 0

  for i in range(N):
    for j in range(M):
      if iceberg[i][j] and not visited[i][j]:
        iceberg_cnt += 1
        q = []
        q.append([i,j])

        while q:
          y, x = q.pop()
          if visited[y][x]: continue

          visited[y][x] = True

          for k in range(4):
            ny, nx = y + direction[k][0], x + direction[k][1]
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and iceberg[ny][nx]:
              q.append([ny,nx])

  return iceberg_cnt


def get_data():
  N, M = map(int, input().split())
  iceberg = list(
    list(map(int, input().split())) for _ in range(N)
  )

  return [N, M, iceberg]

if __name__ == "__main__":
  N, M , iceberg = get_data()
  result = 0
  print_result = False
  direction = [
    [-1,0], [1,0], [0,-1], [0,1]
  ]

  while True:
    result += 1
    iceberg = melt_iceberg()

    if not iceberg:
      break

    cnt = count_iceberg()
    # for line in iceberg:
    #   print(line)
    if cnt > 1:
      print_result = True
      break

  if print_result:
    print(result)
  else:
    print(0)
