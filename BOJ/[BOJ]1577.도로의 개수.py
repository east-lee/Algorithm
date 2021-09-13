


def get_data():
  N, M = map(int, input().split())
  k = int(input())
  blocker = [
    list(map(int, input().split())) for _ in range(k)
  ]

  for i in range(k):
    a, b, c, d = blocker[i]
    if (a**2+b**2) > (c**2 + d**2):
      blocker[i] = [c,d,a,b]

  return [N+1, M+1, blocker]


if __name__ == "__main__":
  N, M, blocker = get_data()

  dp = [
    [0] * M for _ in range(N)
  ]

  for i in range(1, N):
    if [i-1,0,i,0] in blocker:
      break
    else:
      dp[i][0] = 1

  for j in range(1, M):
    if [0, j-1, 0, j] in blocker: break
    else:
      dp[0][j] = 1


  for i in range(1,N):
    for j in range(1, M):
      a = dp[i][j-1] if [i,j-1,i,j] not in blocker else 0
      b = dp[i-1][j] if [i-1, j, i, j] not in blocker else 0
      dp[i][j] = a + b

  print(dp[-1][-1])