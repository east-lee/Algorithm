




def main():
  global cant_col, cant_row
  result = False
  for i in range(N):
    for j in range(N):
      if not game_board[i][j]: continue
      if cant_row[j]: continue
      cant_row[j] = True
      print(j+1)
      result = True
      break

  return result


def make_board(N):
  game_board = [
    [True] * N for _ in range(N)
  ]

  for i in range(N):
    game_board[i][i] = False
    game_board[i][N-1-i] = False

  return game_board


if __name__ == "__main__":
  N = int(input())
  game_board = make_board(N)

  cant_col = [False] * N
  cant_row = [False] * N

  if not main(): print(-1)