from collections import deque
import sys

def bfs():
  global result

  q = deque()
  check = [
    [-1] * N for _ in range(N)
  ]
  cnt = 0
  for i in range(len(pos_position)):
    if visited[i]:
      y, x = pos_position[i]
      check[y][x] = 0
      q.append(pos_position[i])

  while q:
    y, x = q.popleft()
    for k in range(4):
      ny, nx = y + direction[k][0], x + direction[k][1]

      if 0<=ny<N and 0<=nx<N and check[ny][nx] == -1:
        if arr[ny][nx] == 0:
          check[ny][nx] = check[y][x] + 1
          q.append([ny,nx])
          cnt = max(cnt, check[ny][nx])
        if cnt >= result: return

  for i in range(N):
    for j in range(N):
      if arr[i][j] == 0 and check[i][j] == -1:
        return
  result = min(result, cnt)


def pick_start(index = 0, picked_num = 0):
  global visited
  if picked_num == M:
    bfs()
    return

  for i in range(index, len(pos_position)):
    if not visited[i]:
      visited[i] = 1
      pick_start(index+1, picked_num + 1)
      visited[i] = 0

def find_pos_position():
  global arr
  pos_position = []
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 2:
        pos_position.append([i,j])
        arr[i][j] = 0

  return pos_position

def get_data():
  N, M = map(int, input().split())
  arr = [
    list(map(int, input().split())) for _ in range(N)
  ]

  return [N, M, arr]


if __name__ == "__main__":
  N, M, arr = get_data()
  pos_position = find_pos_position()
  direction = [
    [-1,0], [1,0], [0,-1], [0,1]
  ]
  result = sys.maxsize


  visited = [0] * len(pos_position)
  pick_start()

  print(result) if result != sys.maxsize else print(-1)

