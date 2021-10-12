def check_range(i,j):
  if 0<=i<N and 0<=j<N:
    return True
  return False

def check_pos(i,j,dir):
  current_height = arr[i][j]
  visited = [0] * N
  for k in range(1, N):
    y, x = i + direction[dir][0] * k, j + direction[dir][1] * k
    # if i == 3 and j == 0 and dir == 0:
    #   print(visited, k)
    if abs(arr[y][x] - current_height) >= 2:
      return False
    elif arr[y][x] == current_height:
      continue
    elif arr[y][x] == current_height + 1:
      for m in range(1,L+1):
        cy, cx = y - direction[dir][0]*m, x - direction[dir][1] * m
        check_visited = cy if dir == 1 else cx
        if check_range(cy, cx) and not visited[check_visited] and arr[cy][cx] == current_height:
          visited[check_visited] = 1
          continue
        else:
          return False
      current_height += 1
    elif arr[y][x] == current_height - 1:
      for m in range(L):
        cy, cx = y + direction[dir][0] * m, x + direction[dir][1] * m
        check_visited = cy if dir == 1 else cx
        if check_range(cy, cx) and not visited[check_visited] and arr[cy][cx] == current_height - 1:
          visited[check_visited] = 1
          continue
        else:
          return False
      current_height -= 1
  # print(i, j)
  # print(visited)
  return True

def get_data():
  N, L = map(int, input().split())
  arr = list(
    list(map(int,input().split())) for _ in range(N)
  )

  return [N, L, arr]

if __name__ == "__main__":
  N, L, arr =  get_data()
  result = 0
  direction = [
    [0, 1], [1,0]
  ]

  for i in range(N):
    start_y_row, start_x_row, start_y_col, start_x_col = i, 0, 0, i
    result += 1 if check_pos(start_y_row, start_x_row, 0) else 0
    result += 1 if check_pos(start_y_col, start_x_col, 1) else 0

  print(result)