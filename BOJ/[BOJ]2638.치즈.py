def find_melt_cheese(surface_list):
  melt_list = []

  for i, j in surface_list:
    count = 0
    for k in range(4):
      y, x = i+direction[k][0], j+direction[k][1]

      if 0<=y<N and 0<=x<M and arr[y][x] == 0:
        count += 1
      if count == 2:
        break
    if count == 2 and [i,j] not in melt_list:
      melt_list.append([i,j])
  return melt_list


def find_surface():

  surface_list = []

  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1:
        surface_list.append([i,j])
        break
    for j in range(M-1,-1,-1):
      if arr[i][j] == 1:
        surface_list.append([i, j])
        break

  for j in range(M):
    for i in range(N):
      if arr[i][j] == 1:
        surface_list.append([i, j])
        break
      for i in range(N - 1, -1, -1):
        if arr[i][j] == 1:
          surface_list.append([i, j])
          break

  return surface_list

def main():
  global cheese_total_cnt, arr

  time = 0
  while cheese_total_cnt > 0:
    time += 1
    surface_list = find_surface()
    melt_list = find_melt_cheese(surface_list)
    if not melt_list:
      break
    cheese_total_cnt -= len(melt_list)

    for i, j in melt_list:
      arr[i][j] = 0

  return time

def cheese_cnt():

  cnt = 0

  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1:
        cnt += 1

  return cnt

def get_data():
  N, M = map(int, input().split())
  arr = []

  for _ in range(N):
    line = list(map(int, input().split()))
    arr.append(line)

  return [N, M, arr]


if __name__ == "__main__":
  N, M, arr = get_data()
  cheese_total_cnt = cheese_cnt()
  direction = [
    [-1,0], [1,0], [0,-1], [0,1]
  ]

  print(main())