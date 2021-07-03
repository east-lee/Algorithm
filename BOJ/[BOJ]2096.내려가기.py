def main():
  global max_game, min_game

  for i in range(N-1,0,-1):
    for j in range(3):
      for k in range(3):
        next_y, next_x = i + next_step[k][0], j + next_step[k][1]

        if 0<=next_x<3:
          max_game[next_y][next_x] = max(max_game[next_y][next_x], max_game[i][j] + GAME_BOARD[next_y][next_x])
          min_game[next_y][next_x] = min(min_game[next_y][next_x], min_game[i][j] + GAME_BOARD[next_y][next_x])


def init_setting():
  global max_game, min_game

  for j in range(3):
    max_game[N-1][j] = GAME_BOARD[N-1][j]
    min_game[N-1][j] = GAME_BOARD[N-1][j]


def get_data():
  N = int(input())
  GAME_BOARD = []

  for _ in range(N):
    num_line = list(map(int,input().split()))
    GAME_BOARD.append(num_line)

  return [N, GAME_BOARD]

if __name__ == "__main__":
  N, GAME_BOARD = get_data()
  max_num, min_num = 9*100000, 0

  min_game = list([max_num] * 3 for _ in range(N))
  max_game = list([min_num] * 3 for _ in range(N))

  init_setting()

  next_step = [
    [-1,-1], [-1,0], [-1,1]
  ]

  main()

  max_result, min_result = max(max_game[0]), min(min_game[0])
  print(max_result, min_result)

#https://www.acmicpc.net/problem/2096