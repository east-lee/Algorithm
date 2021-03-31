def solution(i,j):
  global result
  check = list([0]*M for _ in range(N))

  q = []
  q.append([i,j])
  check[i][j] = 1
  new_q = []
  cnt = 0
  while q:
    y,x = q.pop()
    for k in range(4):
      next_y, next_x = y + direction[k][0] , x+direction[k][1]
      if 0<=next_y<N and 0<=next_x<M and not check[next_y][next_x] and MAP[next_y][next_x] == 'L':
        new_q.append([next_y,next_x])
        check[next_y][next_x] = 1
    if not q and new_q:
      cnt += 1
      q = new_q
      new_q = []
  if cnt > result:
    result = cnt



direction = [[-1,0],[1,0],[0,1],[0,-1]]
if __name__ == "__main__":
  N,M = map(int,input().split())

  MAP = list(list(input()) for _ in range(N))
  result = 0

  for i in range(N):
    for j in range(M):
      if MAP[i][j] == "L":
        solution(i,j)
  print(result)