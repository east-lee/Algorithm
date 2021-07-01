def refill_fileld():
  global field

  new_field = list(['.']*M for _ in range(N))

  for j in range(M):
    start_i = N-1
    for i in range(N-1,-1,-1):
      if field[i][j] != '.':
        new_field[start_i][j] = field[i][j]
        start_i -= 1
  field = new_field


def bomb(bomb_list):
  global field

  for i, j in bomb_list:
    field[i][j] = '.'

  return True

def Puyo(i,j):
  q = []
  bomb_list = [[i,j]]
  q.append([i,j])
  color = field[i][j]
  cnt = 1

  while q:
    y,x = q.pop()
    for k in range(4):
      ny, nx = y + direction[k][0], x + direction[k][1]
      if 0<=ny<N and 0<=nx<M and field[ny][nx] == color and [ny,nx] not in bomb_list:
        q.append([ny,nx])
        bomb_list.append([ny,nx])
        cnt += 1

  if cnt >= 4:
    return bomb(bomb_list)
  return False

def searching():
  global result

  cnt = 0

  for i in range(N):
    for j in range(M):
      if field[i][j] != '.':
        if Puyo(i,j): cnt += 1

  if cnt:
    result += 1
    refill_fileld()
    searching()
    return True

  return False

if __name__ == "__main__":
  N, M, result = 12, 6, 0
  field = list(list(input()) for _ in range(12))
  direction = [
    [-1,0],[1,0],[0,-1],[0,1]
  ]

  searching()

  print(result)