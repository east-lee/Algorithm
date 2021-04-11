from collections import deque

def solution():
  dp = [[-1]*1001 for _ in range(1001)]
  dp[1][0] = 0
  q = deque([(1,0)])
  while q:
    x,y = q.popleft()
    if x <= 1000:
      if dp[x][x] == -1:
        dp[x][x] = dp[x][y] + 1
        q.append((x,x))
    if x+y <= 1000:
      if dp[x+y][x] == -1:
        dp[x+y][y] = dp[x][y] + 1
        q.append((x+y,y))
    if x-1>-1:
      if dp[x-1][y] == -1:
        dp[x-1][y] = dp[x][y] + 1
        q.append((x-1,y))
    if x == s: break

  result = 1000000000000
  for i in dp[s]:
    if result > i and i != -1: result =i
  print(result)

if __name__ == "__main__":
  s = int(input())

  solution()


