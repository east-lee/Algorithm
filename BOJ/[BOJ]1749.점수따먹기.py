import sys


def get_data():
  N, M = map(int, input().split())

  game_board = [
    list(map(int,input().split())) for _ in range(N)
  ]

  return [N,M,game_board]


if __name__ == "__main__":
  N, M, game_board = get_data()
  result = -sys.maxsize

  dp = [
    [0] * (M+1) for _ in range(N+1)
  ]

  for i in range(1,N+1):
    for j in range(1,M+1):
      dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + game_board[i-1][j-1]


  for i in range(1,N+1):
    for j in range(1,M+1):
      for m in range(i,N+1):
        for n in range(j,M+1):
          check_num = dp[m][n] - dp[m][j-1] - dp[i-1][n] + dp[i-1][j-1]
          result = max(result,check_num)

  print(result)
