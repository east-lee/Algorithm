def get_data():
  N = int(input())
  game_board = [
    list(map(int,input().split())) for _ in range(N)
  ]

  return [N, game_board]

if __name__ == "__main__":
  N, game_board = get_data()
  dp = [
    [0] * N for _ in range(N)
  ]
  dp[0][0] = 1

  for i in range(N):
    for j in range(N):
      if i == j == N-1:
        break

      jump = game_board[i][j]
      jump_to_right = j + jump
      jump_to_down = i + jump

      if jump_to_right < N: dp[i][jump_to_right] += dp[i][j]
      if jump_to_down < N: dp[jump_to_down][j] += dp[i][j]
  print(dp[-1][-1])