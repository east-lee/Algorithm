def main():
  global maze
  y, x = 50, 50
  min_i, min_j, max_i, max_j = list(50 for _ in range(4))
  seeing_direction = 0
  for i in range(N):
    action = moving_list[i]

    if action == 'F':
      y, x = y+direction[seeing_direction][0], x + direction[seeing_direction][1]
      maze[y][x] = '.'
      min_i, min_j, max_i, max_j = min(min_i,y),min(min_j,x),max(max_i,y),max(max_j,x)
    elif action == 'R':
      seeing_direction = seeing_direction + 1 if seeing_direction != 3 else 0
    elif action == 'L':
      seeing_direction = seeing_direction - 1 if seeing_direction != 0 else 3

  return [min_i,min_j,max_i,max_j]

if __name__ == "__main__":
  maze = list(['#']*100 for _ in range(100))
  N = int(input())
  moving_list = list(input())
  direction=[[1,0],[0,-1],[-1,0],[0,1]] #오른쪽으로돌면 +1 왼쪽으로돌면 -1
  maze[50][50] = '.'
  min_i,min_j,max_i,max_j = main()

  for i in range(100):
    if min_i<=i<=max_i:
      for j in range(100):
        if min_j<=j<=max_j:
          print(maze[i][j],end='')
      print()
