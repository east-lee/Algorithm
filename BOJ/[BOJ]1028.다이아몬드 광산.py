def find_can(y,x):
  global max_diamond_length

  cnt = 0

  while True:
    left_y, left_x,right_y, right_x = y+ cnt*direction[1][0], x+cnt*direction[1][1], y+cnt*direction[0][0], x+cnt*direction[0][1]
    if not check_bound(left_y,left_x,right_y,right_x):
      break
    if cnt+1 > max_diamond_length and  check_diamond(left_y,left_x,right_y,right_x,cnt):
      max_diamond_length = max(max_diamond_length,cnt+1)
    cnt += 1

def check_bound(left_y,left_x,right_y,right_x):
  if 0<=left_y<R and 0<=right_y<R and 0<=left_x<C and 0<=right_x<C and mount[left_y][left_x] == 1 and mount[right_y][right_x] == 1:
    return True
  return False


def check_diamond(y1,x1,y2,x2,cnt):
  for i in range(1,cnt+1):
    ly,lx,ry,rx = y1+i*direction[0][0], x1+i*direction[0][1] , y2+i*direction[1][0], x2+i*direction[1][1]
    if not check_bound(ly,lx,ry,rx):
      return False
  return True


if __name__ == "__main__":
  R, C = map(int,input().split())
  mount = list(list(map(int,list(input()))) for _ in range(R))
  max_diamond_length = 0
  direction = [[1,1],[1,-1]]

  for i in range(R):
    for j in range(C):
      if mount[i][j] == 0 or (max_diamond_length >= 2 and (i+max_diamond_length-1 >= R or j+max_diamond_length-1>=C or j-max_diamond_length+1 <0 or i-max_diamond_length+1<0)): continue
      find_can(i,j)

  print(max_diamond_length)
