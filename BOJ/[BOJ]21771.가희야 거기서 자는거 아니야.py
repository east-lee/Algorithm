def check(i,j):
  right, down = False, False
  for y in range(R):
    if arr[y][j] == 'P':
      down = True
      break
  for x in range(C):
    if arr[i][x] == 'P':
      right = True
      break
  if right and down: return  True
  return False

if __name__ == "__main__":
  R, C = map(int,input().split())
  x1,y1,x2,y2 = map(int,input().split())

  arr = list(list(input()) for _ in range(R))
  result = 0
  for i in range(R):
    for j in range(C):
      if arr[i][j] == 'G':
        if check(i,j):
          result = 1
          break
    if result: break
  print(result)