#문제조건
# 1. 아기상어는 자신보다 큰 물고기는 먹지도 지나가지도 못한다
# 2. 자신과 크기가 같다면 지나갈수는 있지만 먹지는 못한다
# 3. 자신보다 작으면 먹는다.
#다른조건
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 엄마 상어에게 도움을 요청한다
# 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 간다.
# 1마리보다 많으면 가장 가까운 물고기를 먹으러 간다.
# 자신의 크기는 자신의 크기와 같은 수의 물고기를 먹을 때마다 1증가한다.

from collections import deque

def record_time(can_eat):
  visited = list([0]*N for _ in range(N))
  i, j = baby_shark
  visited[i][j] = 1
  q = deque()
  q.append([i,j,0])
  while q:
    y, x, time = q.popleft()
    if [y,x] == can_eat:
      return time

    for k in range(4):
      ny, nx = y+direction[k][0], x+direction[k][1]
      if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0 and sea[ny][nx] <= baby_shark_size:
        visited[ny][nx] = 1
        q.append([ny,nx,time+1])

  return 20*21


def check_time(can_eat_list):
  min_time = 20*20
  min_time_location = []

  for can_eat in can_eat_list:
    time = record_time(can_eat)
    if min_time > time:
      min_time = time
      min_time_location = []
      min_time_location.append(can_eat)
    elif min_time == time:
      min_time_location.append(can_eat)
  if not min_time_location:
    return [min_time, False]

  return [min_time, min_time_location[0]]



def find_can_eat():
  can_eat_list = []

  for i in range(N):
    for j in range(N):
      if sea[i][j] != 9 and sea[i][j] != 0 and sea[i][j] < baby_shark_size:
        can_eat_list.append([i,j])

  return can_eat_list

def main():
  global sea, baby_shark, baby_shark_size, eating_cnt
  time = 0
  while True:
    can_eat_list = find_can_eat()
    if len(can_eat_list) == 0: return time

    min_time, location = check_time(can_eat_list)
    # print(location,min_time,baby_shark)
    if not location: return time
    i,j = baby_shark
    y,x = location
    time += min_time
    sea[i][j] = 0
    sea[y][x] = 9
    eating_cnt += 1
    baby_shark = [y,x]

    if eating_cnt == baby_shark_size:
      baby_shark_size += 1
      eating_cnt = 0

  return time




def find_baby_shark(sea):
  for i in range(N):
    for j in range(N):
      if sea[i][j] == 9:
        return [i,j]

def get_data():

  N = int(input())
  sea = list(list(map(int,input().split())) for _ in range(N))

  return [N, sea]


if __name__ == "__main__":
  N , sea = get_data()
  baby_shark_size = 2
  baby_shark = find_baby_shark(sea)
  eating_cnt = 0
  direction = [
    [1,0],[-1,0],[0,1],[0,-1]
  ]
  print(main())