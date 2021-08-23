def make_group(y, x, k, s_cnt, y_cnt, route):
  global visited, result

  if y_cnt >= 4:
    return
  if k == 7:
    route.sort()
    if route not in result:
      result.append(route)
    return
  for sy, sx in route:
    for dir in range(4):
      next_y, next_x = sy+direction[dir][0], sx+direction[dir][1]
      if 0<=next_y<N and 0<=next_x<N and not visited[next_y][next_x]:
        visited[next_y][next_x] = True
        make_group(next_y, next_x, k+1, s_cnt + 1, y_cnt, route + [[next_y, next_x]]) if sit_info[next_y][next_x] == "S" else make_group(next_y, next_x, k+1, s_cnt, y_cnt + 1, route + [[next_y, next_x]])
        visited[next_y][next_x] = False


def get_data():
  N = 5
  sit_info = list(list(input()) for _ in range(N))

  return [N, sit_info]

if __name__ == "__main__":
  N, sit_info = get_data()
  result = []

  direction = [
    [-1,0], [1,0], [0,-1], [0,1]
  ]

  visited = [
    [False] * N for _ in range(N)
  ]

  for i in range(N):
    for j in range(N):
      if sit_info[i][j] == "S":
        make_group(i, j, 0, 1, 0, [[i,j]])
      visited[i][j] = True
  print(len(result))