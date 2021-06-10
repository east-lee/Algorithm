def check_height(arr,h):
  for i,j in arr:
    if farm[i][j] > h:
      return False
  return True

def main(i,j,h):
  global check

  after_check_list = []
  q = [[i,j]]
  while q:
    y,x = q.pop()
    if check[y][x]: continue
    check[y][x] = 1

    for k in range(8):
      next_y, next_x = y+direction[k][0], x+direction[k][1]
      if 0<=next_y<N and 0<=next_x<M and farm[next_y][next_x] == h:
        q.append([next_y,next_x])
      elif 0<=next_y<N and 0<=next_x<M:
        after_check_list.append([next_y,next_x])
        
  if check_height(after_check_list,h):
    return 1
  else: return 0

if __name__ == "__main__":
  N, M = map(int,input().split())
  direction = [[-1,0],[1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]
  farm = list(list(map(int,input().split())) for _ in range(N))
  result = 0
  check = list([0]*M for _ in range(N))

  for i in range(N):
    for j in range(M):
      if check[i][j]: continue
      r = main(i,j,farm[i][j])
      result += r
  print(result)
