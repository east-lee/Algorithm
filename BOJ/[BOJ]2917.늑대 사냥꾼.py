import sys
from collections import deque
from copy import deepcopy

def calc_distance(A,B):

  return abs(A[0]-B[0]) + abs(A[1]-B[1])

def find_min_distance(me):

  min_dist = sys.maxsize

  for tree in tree_list:
    dist = calc_distance(me,tree)
    min_dist = min(min_dist, dist)

  return min_dist

def find_position():
  position_dict = {
    'V':0, 'J':1, '+':2
  }
  position = [[] for _ in range(3)] # position 0:my position / 1:shelter / 2: tree

  for i in range(N):
    for j in range(M):
      if forest[i][j] == '.': continue
      position[position_dict[forest[i][j]]].append([i, j])

  for i in range(2):
    position[i] = position[i][0]

  return position


def get_data():
  N, M = map(int, input().split())

  forest = [
    list(input()) for _ in range(N)
  ]

  return [N, M, forest]


if __name__ == "__main__":
  N, M, forest = get_data()
  me, shelter, tree_list = find_position()
  direction = [
    [-1,0], [1,0], [0,-1], [0,1]
  ]

  result = find_min_distance(me)
  # visited = [[0] * M for _ in range(N)]
  visited = {}

  dq = deque()
  dq.append([me[0],me[1],result, visited])

  while dq:
    y, x, mid_result, v = dq.popleft()
    # v[y][x] = 1
    visited[f'[{y},{x}]'] = 1
    if [y,x] == shelter:
      result = min(result, mid_result)
      break
    pos_position = []
    m_dist = 0

    for k in range(4):
      ny, nx = y + direction[k][0], x + direction[k][1]
      # if 0<=ny<N and 0<=nx<M and v[ny][nx] == 0:
      if 0<=ny<N and 0<=nx<M and f'[{ny},{nx}]' not in v.keys():
        dist = find_min_distance([ny, nx])
        if dist > m_dist:
          pos_position = []
          pos_position.append([ny,nx])
          m_dist = dist
        elif dist == m_dist:
          pos_position.append([ny,nx])

    for next_y, next_x in pos_position:
      new_visited = deepcopy(v)
      dq.append([next_y, next_x, min(mid_result,m_dist), new_visited])

  print(result)






