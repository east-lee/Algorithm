def main():
  arr = list(list(0 for _ in range(N)) for _ in range(N))
  i,j = -1,0
  cnt = N**2
  dir_idx = 0
  y,x=0,0
  while cnt>0:
    next_i, next_j = i+direction[dir_idx][0], j+direction[dir_idx][1]

    if 0>next_i or 0>next_j or N <= next_j or N <= next_i or arr[next_i][next_j] != 0:
      dir_idx = dir_idx + 1 if dir_idx < 3 else 0
    i , j = i + direction[dir_idx][0], j + direction[dir_idx][1]

    arr[i][j] = cnt
    cnt -= 1
    if cnt + 1 == find_num:
      y,x = i , j

  for i in arr:
    for j in i:
      print(j,end=' ')
    print()
  print(y+1, x+1)


if __name__ == "__main__":
  N = int(input())
  find_num = int(input())
  direction = [[1,0],[0,1],[-1,0],[0,-1]]
  main()