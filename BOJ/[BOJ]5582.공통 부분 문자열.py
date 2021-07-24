def get_max_length(arr):

  visited = [
    [0] * (M+1) for _ in range(N+1)
  ]

  max_length = 0

  for i in range(1,N+1):
    for j in range(1,M+1):
      if arr[i][j] == 0 or visited[i][j] == 1:
        visited[i][j] = 1
        continue
      if string1[i-1] != string2[j-1]: continue
      check_value = arr[i][j]
      visited[i][j] = 1

      length = 1
      y, x = i + 1, j + 1

      while 0<=y<=N and 0<=x<=M:
        if arr[y][x] == check_value + 1 and string1[y-1] == string2[x-1]:

          check_value += 1
          visited[y][x] = 1
          y += 1
          length += 1
          x += 1
        else: break

      max_length = max(max_length, length)
  return max_length

def LCS():


  dp = [
    [0] * (M+1) for _ in range(N+1)
  ]

  for i in range(N):
    for j in range(M):

      if string1[i] == string2[j]:
        dp[i+1][j+1] = dp[i][j] + 1
      else:
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])


  return  get_max_length(dp)


def get_data():
  String_data = list(list(input()) for _ in range(2))

  return String_data


if __name__ == "__main__":
  string1, string2 = get_data()
  N = len(string1)
  M = len(string2)

  result = LCS()
  print(result)
