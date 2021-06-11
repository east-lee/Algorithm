def check_5stone(i,j):

  for k in range(4):
    cnt = 1

    for y_add, x_add in direction[k]:
      y, x = i, j
      y += y_add
      x += x_add

      while 0<=y<18 and 0<=x<18 and board[y][x] == board[i][j]:
        cnt += 1
        y += y_add
        x += x_add
    if cnt == 5:
      return True
  return False


if __name__ == "__main__":
  N = int(input())
  result = -1

  board = list([0]*N for _ in range(N))

  direction = [
    [[0,-1],[0,1]],
    [[1,0],[-1,0]],
    [[-1,1],[1,-1]],
    [[1,1],[-1,-1]]
  ]

  for i in range(N):
    stone = 'W'
    if i % 2 == 0: stone = 'B'
    y, x = map(int,input().split())
    if result != -1: continue
    y, x = y-1, x-1
    board[y][x] = stone
    if check_5stone(y,x):
      result = i+1
  print(result)