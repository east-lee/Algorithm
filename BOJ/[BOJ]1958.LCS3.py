# 3개의 문자열의 LCS => 3차 배열?

def get_data():
  n = 3
  string_list = [
    [" "] + list(input()) for _ in range(n)
  ]

  return string_list

if __name__ == "__main__":
  string_list = get_data()
  dp = [
    [
      [0]*(len(string_list[0])) for _ in range(len(string_list[1]))
    ] for _ in range(len(string_list[2]))
  ]

  for i in range(1, len(string_list[2])):
    for j in range(1, len(string_list[1])):
      for k in range(1, len(string_list[0])):
        if string_list[0][k] == string_list[1][j] == string_list[2][i]:
          dp[i][j][k] = dp[i-1][j-1][k-1] + 1
        else:
          dp[i][j][k] = max(
            dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1], dp[i-1][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1]
          )

  print(dp[-1][-1][-1])