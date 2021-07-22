from collections import deque

def BFS():
  global not_break_check, break_check

  q = deque()
  q.append([Hx, Hy, 0, 0])

  while q:

    y, x, breaking, cnt = q.popleft()

    if y == Ex and x == Ey:
      return cnt

    for k in range(4):
      i, j = y + direction[k][0], x + direction[k][1]

      if 0<= i < N and 0<= j < M:
        if not breaking:
          if not_break_check[i][j] == 0 and maze[i][j] == 0:
            q.append([i,j,breaking,cnt + 1])
            not_break_check[i][j] = 1
          elif break_check[i][j] == 0 and maze[i][j] == 1:
            q.append([i, j, 1, cnt + 1])
            break_check[i][j] = 1
        else:
          if maze[i][j] == 0 and break_check[i][j] == 0:
            q.append([i,j,breaking,cnt + 1])
            break_check[i][j] = 1
  return -1





def make_check_maze():
  check_maze = [
    list([0]*M for _ in range(N))
    for _ in range(2)
  ]

  for maze in check_maze: maze[Hx][Hy] = 1

  return check_maze


def get_data():
  map_data = []

  for i in range(3):
    data1, data2 = map(int, input().split())

    if i != 0:
      data1 -= 1
      data2 -= 1

    map_data.extend([data1, data2])

  maze = [list(map(int,input().split())) for _ in range(map_data[0])]

  map_data.append(maze)

  return map_data


if __name__ == "__main__":
  N, M, Hx, Hy, Ex, Ey, maze = get_data()
  not_break_check, break_check = make_check_maze()
  direction = [
    [-1,0],[1,0],[0,-1],[0,1]
  ]


  result = BFS()
  print(result)
