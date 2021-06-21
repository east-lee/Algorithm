def get_maze():
  maze = list(list(map(int,input().split())) for _ in range(N))

  return maze

def init_setting():
  global maze

  for i in range(1,N):
    maze[i][0] = maze[i-1][0] + maze[i][0]

  for j in range(1,M):
    maze[0][j] = maze[0][j-1] + maze[0][j]


if __name__ == "__main__":
  N, M = map(int,input().split())
  maze = get_maze()
  init_setting()

  for i in range(1,N):
    for j in range(1,M):
      maze[i][j] = maze[i][j] + max(maze[i-1][j], maze[i][j-1])

  print(maze[N-1][M-1])
