from copy import deepcopy

def main():
  global mine
  dfs(mine,0,[1,1],0)


def dfs(arr,rotate_idx,position,cnt):
  global result

  y,x = position
  next_y, next_x = y + rotate_direction[rotate_idx][0], x + rotate_direction[rotate_idx][1]
  if arr[next_y][next_x] != '#':
    rotate_idx += 1
  if rotate_idx == 4:
    if cnt > result and check_zero(arr):
      result = cnt
    return

  next_y, next_x = y + rotate_direction[rotate_idx][0], x + rotate_direction[rotate_idx][1]
  zero_exit = False
  minus_arr = []

  for k in range(8):
    i,j = next_y + direction[k][0], next_x+direction[k][1]
    if 0<=i<N and 0<=j<N:
      if arr[i][j] == 0:
        zero_exit = True
        break
      elif arr[i][j] != '#' and arr[i][j] != '.' and arr[i][j] != '':
        minus_arr.append([i,j])

  new_arr = deepcopy(arr)
  new_arr[next_y][next_x] = ''
  dfs(new_arr,rotate_idx,[next_y,next_x],cnt)

  if not zero_exit:
    mine_new_arr = deepcopy(arr)
    for minus_i, minus_j in minus_arr:
      mine_new_arr[minus_i][minus_j] = mine_new_arr[minus_i][minus_j]-1
    mine_new_arr[next_y][next_x] = '.'
    dfs(mine_new_arr,rotate_idx,[next_y,next_x],cnt + 1)

def check_zero(arr):
  non_zero = False

  for i in range(N):
    if arr[0][i] or arr[i][0] or arr[N-1][i] or arr[i][N-1]:
      non_zero= True
      break
  if non_zero:
    return False
  else: return True






if __name__ == "__main__":
  N = int(input())
  mine = list(list(input()) for _ in range(N))
  result = 0
  direction = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
  rotate_direction = [[0,1],[1,0],[0,-1],[-1,0]]

  for i in range(N):
    for j in range(N):
      try:
        mine[i][j] = int(mine[i][j])
      except:
        continue

  if N<3:
    print(0)
  else:
    main()
    print((result+(N-4)**2) if N>=5 else result)
