def main(i,j):
  global home_list
  q = []
  q.append([i,j])
  cnt = 0
  while q:
    y,x = q.pop()
    if home_list[y][x] == 0:continue
    home_list[y][x] = 0
    cnt += 1
    for k in range(4):
      ny, nx = y+direction[k][0], x+direction[k][1]
      if 0<=ny<N and 0<=nx<N and home_list[ny][nx] == 1:
        q.append([ny,nx])
  return cnt

if __name__ == "__main__":
  N = int(input())
  home_list = list(list(map(int,list(input()))) for _ in range(N))
  home_cnt_list = []
  direction = [[-1,0],[0,-1],[0,1],[1,0]]
  for i in range(N):
    for j in range(N):
      if home_list[i][j] == 1:
        home_cnt_list.append(main(i,j))

  print(len(home_cnt_list))
  home_cnt_list.sort()
  for home_cnt in home_cnt_list:

    print(home_cnt)





