# 가능한 경로가 여러개 일 수 있다! 즉 네방향중 나무와의 최대거리가 가장 큰 경우가 여러개 일 수 있다.
# 위 조건으로 문제 다시 풀어보기


import sys


def calc_distance(A, B):

  return abs(A[0]-B[0]) + abs(A[1]-B[1])


def find_position():
  tree, me, shelter = [[] for _ in range(3)]

  for i in range(N):
    for j in range(M):
      check = forest[i][j]
      if check == '.':  continue
      elif check == '+':  tree.append([i,j])
      elif check == 'V':  me = [i,j]
      elif check == 'J':  shelter = [i,j]

  return [tree, me, shelter]


def get_data():
  N, M = map(int, input().split())

  forest = [
    list(input()) for _ in range(N)
  ]

  return [N, M, forest]

if __name__ == "__main__":
  N, M, forest = get_data()
  tree, me, shelter = find_position()
  direction = [[-1,0], [1,0], [0,-1], [0,1]]
  result = sys.maxsize

  visited = [[False]*M for _ in range(N)]
  visited[me[0]][me[1]] = True

  for t in tree:
    result = min(result, calc_distance(me,t))

  while True:
    if shelter == me:
      break
    y, x = me

    pos_root = []
    for k in range(4):
      ny, nx = y + direction[k][0], x + direction[k][1]
      if 0<=ny<N and 0<=nx<M:
        min_distance = sys.maxsize
        for t in tree:
          distance = calc_distance([ny,nx], t)
          min_distance = min(min_distance, distance)
        pos_root.append([min_distance,ny,nx])

    pos_root.sort(key = lambda x:-x[0])
    if not pos_root:
      break
    next_distance,next_y, next_x = pos_root[0]

    visited[next_y][next_x] = True
    me = [next_y,next_x]
    result = min(result,next_distance)

  for t in tree:
    result = min(result,calc_distance(shelter,t))

  print(result)



