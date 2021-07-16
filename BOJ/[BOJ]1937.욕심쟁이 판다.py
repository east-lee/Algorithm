from collections import deque


def BFS(i,j):
  print(i,j,'-------------------------')
  max_cnt = 1
  q = deque()
  q.append([i,j,1])

  while q:
    y,x,cnt = q.popleft()
    print(y,x,cnt)
    # max_cnt = max(max_cnt,cnt)
    if dp[y][x] != -1:
      print('i see dp[y][x]', dp[y][x], cnt)
      max_cnt = max(max_cnt, dp[y][x] + cnt)
    else:
      for k in range(4):
        ny, nx = i + direction[k][0], j + direction[k][1]
        if 0 <= ny < N and 0 <= nx < N and forest[y][x] < forest[ny][nx]:
          q.append([ny,nx,cnt+1])
          max_cnt = max(max_cnt, cnt + 1)

  return max_cnt

def get_data():
  N = int(input())
  forest = list()

  dp = list([-1] * N for _ in range(N))

  for _ in range(N):
    new_input = list(map(int,input().split()))
    forest.append(new_input)

  return [N, forest, dp]

if __name__ == "__main__":
  N, forest, dp = get_data()
  direction = [
    [-1,0], [1,0], [0,-1], [0,1]
  ]

  result = 0

  for i in range(N):
    for j in range(N):
      bfs_result = BFS(i,j)
      result = max(result, bfs_result)
      dp[i][j] = bfs_result

  for line in dp: print(line)
  print(result)









