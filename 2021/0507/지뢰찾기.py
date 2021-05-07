def main():
  global arr
  y,x = 1,0
  rotate_idx = 0
  cnt = 0
  while True:
    i, j = y+rotate_direction[rotate_idx][0], x+rotate_direction[rotate_idx][1]
    if i < 0 or j <0 or i>=N or j >= N:break
    if arr[i][j] != '#': rotate_idx += 1
    if rotate_idx == 4: break
    y, x = y + rotate_direction[rotate_idx][0], x + rotate_direction[rotate_idx][1]
    for k in range(8):
      check_i, check_j = y+direction[k][0], x+direction[k][1]
      if (check_j == 0 or check_j == N-1) or (check_i == 0 or check_i == N-1):
        if arr[check_i][check_j] == 0: break
      arr[y][x] = ''
    else:
      for m in range(8):
        check_i, check_j = y + direction[m][0], x + direction[m][1]
        if (check_j == 0 or check_j == N - 1) or (check_i == 0 or check_i == N - 1):
          arr[check_i][check_j] -= 1
      arr[y][x] = '*'
      cnt += 1

  return cnt



if __name__ == "__main__":
  N = int(input())
  arr = list(list(input()) for _ in range(N))

  direction = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
  rotate_direction = [[0,1],[1,0],[0,-1],[-1,0]]

  for i in range(N):
    arr[0][i] = int(arr[0][i])
    arr[i][0] = int(arr[i][0])
    arr[N-1][i] = int(arr[N-1][i])
    arr[i][N-1] = int(arr[i][N-1])

  cnt = main()

  print(cnt+(N-4)**2 if N>4 else cnt)
