def main():
  global result_map
  for i in range(N):
    for j in range(N):
      if mine_map[i][j] == '.':
        cnt = 0
        for k in range(8):
          y, x = i+direction[k][0], j+direction[k][1]
          if 0<=y<N and 0<=x<N and mine_map[y][x] != '.':
            cnt += int(mine_map[y][x])
        result_map[i][j] = cnt if cnt < 10 else 'M'
      else: result_map[i][j] = '*'

if __name__ == "__main__":
  N = int(input())
  mine_map = list(list(input()) for _ in range(N))
  direction = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
  result_map = list([0]*N for _ in range(N))
  main()

  for r_map in result_map:
    for r in r_map:
      print(r,end='')
    print()