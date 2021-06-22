from copy import deepcopy
# direction_num => 0 1 2 3 / 오른쪽 아래 왼쪽 위

def moving_vertical(game_board,dir):
  for i in range(N):
    for j in range(N):
      ni = i
      if dir == 1:
        ni = N - (i+1)
      sumed = False
      for _ in range(2):
        if sumed: break
        check_i = ni + 1 if not dir else ni - 1
        breaker= False

        while 0<= check_i < N:
          if game_board[check_i][j] != 0:
            breaker = True
            break
          check_i = check_i + 1 if not dir else check_i - 1

        if breaker and game_board[check_i][j] == game_board[ni][j]:
          game_board[ni][j] += game_board[check_i][j]
          game_board[check_i][j] = 0
          sumed = True
        elif breaker and not game_board[ni][j]:
          game_board[ni][j] = game_board[check_i][j]
          game_board[check_i][j] = 0

  return game_board

def moving_horizontal(game_board,dir):
  for i in range(N):
    for j in range(N):
      nj = j
      if dir == 1:
        nj = N - (j+1)
      sumed = False
      for _ in range(2):
        if sumed: break
        check_j = nj + 1 if not dir else nj - 1
        breaker= False

        while 0<= check_j < N:
          if game_board[i][check_j] != 0:
            breaker = True
            break
          check_j = check_j + 1 if not dir else check_j - 1

        if breaker and game_board[i][check_j] == game_board[i][nj]:
          game_board[i][nj] += game_board[i][check_j]
          game_board[i][check_j] = 0
          sumed = True
        elif breaker and not game_board[i][nj]:
          game_board[i][nj] = game_board[i][check_j]
          game_board[i][check_j] = 0
  return game_board



def get_max_num(game_board):
  max_num = 0

  for i in range(N):
    for j in range(N):
      max_num = max(max_num, game_board[i][j])

  return max_num


def moving_game_board(direction_num, game_board):

  if direction_num == 0 or direction_num == 1:
    return moving_vertical(game_board,direction_num)

  return moving_horizontal(game_board,direction_num - 2)


def DFS(k, game_board):
  global result

  if k == 5:
    max_num = get_max_num(game_board)
    result = max(result, max_num)
    return

  for direction_num in range(4):
    copy_game_board = deepcopy(game_board)
    next_game_board = moving_game_board(direction_num, copy_game_board)
    DFS(k+1, next_game_board)


def get_data():
  N = int(input())
  game_board = list(list(map(int,input().split())) for _ in range(N))

  return [N, game_board]

if __name__ == "__main__":
  N, game_board = get_data()
  result = 0
  DFS(0, game_board)
  print(result)