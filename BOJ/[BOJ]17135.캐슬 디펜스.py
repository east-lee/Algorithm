from copy import deepcopy

def calc_distance(A, B):

  return abs(A[0] - B[0]) + abs(A[1] - B[1])

def find_enemy(r1, c1, field, limit_N):
  min_length = 100
  min_length_enemy = []

  for i in range(limit_N):
    for j in range(M):
      if field[i][j] == 1:
        distance = calc_distance([r1,c1],[i,j])
        if distance <= D:
          if min_length > distance:
            min_length = distance
            min_length_enemy = []
            min_length_enemy.append([i,j])
          elif min_length == distance:
            min_length_enemy.append([i,j])

  if not min_length_enemy:
    return []
  else:
    min_length_enemy.sort(key=lambda x:x[1])

    return min_length_enemy[0]

def main(archer):
  new_field = deepcopy(field)
  result = 0
  archer_pos = []
  for i in range(3):
    archer_i = [N, archer[i]]
    archer_pos.append(archer_i)

  limit_N = N
  while archer_pos[0][0] >= 0:
    remove_enemy = []
    for r1, c1 in archer_pos:
      re = find_enemy(r1,c1,new_field,limit_N)
      if not re: continue
      elif re not in remove_enemy:
        remove_enemy.append(re)

    result += len(remove_enemy)
    for i,j in remove_enemy:
      new_field[i][j] = 0

    for i in range(3):
      archer_pos[i][0] -= 1
    limit_N -= 1

  return result

def set_archer(k = 0, last_index = -1, result = []):
  global archer_position

  if k == 3:
    archer_position.append(result)
    return

  for i in range(last_index + 1, M):
    set_archer(k+1, i, result + [i])

def get_data():

  N, M, D = map(int, input().split())
  field = list(list(map(int, input().split())) for _ in range(N))

  return [N, M, D, field]


if __name__ == "__main__":
  archer_position = []
  max_result = 0
  N, M, D, field = get_data()
  set_archer()

  for archer in archer_position:
    cnt = main(archer)
    max_result = max(max_result,cnt)

  print(max_result)
