from collections import deque


def get_data():
  w, h = map(int ,input().split())
  building = list(list(input()) for _ in range(h))

  return [w,h,building]


def find_start_position():
  for i in range(h):
    for j in range(w):
      if building[i][j] == "@":
        return [i, j]

def next_fire():
  global building

  fire_position = []

  for i in range(h):
    for j in range(w):
      if building[i][j] == "*":
        fire_position.append([i,j])

  for i, j in fire_position:
    for k in range(4):
      y, x = i+direction[k][0], j+direction[k][1]

      if 0<=y<h and 0<=x<w and building[y][x] != "#":
        building[y][x] = "*"



if __name__ == "__main__":
  TC = int(input())
  direction = [
    [-1,0], [1,0], [0,-1], [0,1]
  ]
  for _ in range(TC):
    w, h, building = get_data()

    visited = [
      [0] * w for _ in range(h)
    ]
    start_y, start_x = find_start_position()
    q = deque()
    q.append([start_y, start_x, 0])
    check_time = -1
    result = "IMPOSSIBLE"
    while q:
      i, j, time = q.popleft()
      if time != check_time:
        check_time = time
        next_fire()
      if visited[i][j]: continue

      visited[i][j] = 1

      for k in range(4):
        next_i, next_j = i + direction[k][0], j + direction[k][1]
        if 0<=next_i<h and 0<=next_j<w and building[next_i][next_j] == ".":
          q.append([next_i, next_j, time + 1])
        elif 0> next_i or h <= next_i or 0 > next_j or w <= next_j:
          result = time + 1
          break
      if result != "IMPOSSIBLE": break
    print(result)