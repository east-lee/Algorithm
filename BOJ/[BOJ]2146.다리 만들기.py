import sys
from collections import deque

def checking(y,x,num):
  global final_visited
  for k in range(4):
    ny, nx = y + direction[k][0], x + direction[k][1]
    if 0<=ny<N and 0<=nx<N and marked_map[ny][nx] != 0 and marked_map[ny][nx] != num:
      final_visited[ny][nx] = 1
      return True
  return False


def make_bridge(y,x,marking_num):
  global result, v

  dq = deque()
  dq.append([y,x,0])

  while dq:
    i, j, cnt = dq.popleft()
    v[i][j] = 1

    if checking(i,j,marked_map[y][x]):
      result = min(cnt, result)
      break
    if cnt-1 >= result:
      break

    for k in range(4):
      ny, nx = i + direction[k][0], j + direction[k][1]
      if 0<=ny<N and 0<=nx<N and not marked_map[ny][nx] and not v[ny][nx]:
        dq.append([ny,nx,cnt+1])



def mark_map(y,x):
  global visited, marked_map

  dq = deque()
  dq.append([y,x])

  while dq:
    i, j = dq.popleft()
    visited[i][j] = 1
    marked_map[i][j] = marked_num
    for k in range(4):
      dy, dx = i+direction[k][0], j+direction[k][1]
      if 0<=dy<N and 0<=dx<N and not visited[dy][dx] and input_map[dy][dx]:
        dq.append([dy,dx])

  return marked_map


def get_data():
  N = int(input())
  input_map = [
    list(map(int, input().split())) for _ in range(N)
  ]

  return [N, input_map]


if __name__ == "__main__":
  N, input_map = get_data()
  visited, marked_map = [[[0] * N for _ in range(N)] for _ in range(2)]
  final_visited = [[0]*N for _ in range(N)]
  direction = [
    [-1,0], [1,0], [0,-1], [0,1]
  ]
  marked_num = 0
  result = sys.maxsize

  for i in range(N):
    for j in range(N):
      if input_map[i][j] and not visited[i][j]:
        marked_num += 1
        mark_map(i,j)

  for i in range(N):
    for j in range(N):
      if marked_map[i][j] and not final_visited[i][j]:
        v = [[0]*N for _ in range(N)]
        make_bridge(i,j,marked_map[i][j])
  print(result)
