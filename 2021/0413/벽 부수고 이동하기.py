def solution():
  q, new_q = [], []
  result = [[[0] * 2 for i in range(M)] for i in range(N)]
  q.append([0,0,1])
  result[0][0][1] = 1
  r = -1
  while q:
    y,x,w = q.pop()
    if y == N-1 and x == M-1:
      r = result[y][x][w]
      break

    for k in range(4):
      i,j = y+direction[k][0], x+direction[k][1]
      if 0<=i<N and 0<=j<M:
        if arr[i][j] == '1' and w == 1:
          result[i][j][0]=result[y][x][1] + 1
          new_q.append([i,j,0])
        elif arr[i][j] == '0' and result[i][j][w] == 0:
          result[i][j][w] = result[y][x][w] + 1
          new_q.append([i,j,w])
    if not q and new_q:
      q = new_q
      new_q=[]
  print(r)

direction = [[1,0],[0,1],[-1,0],[0,-1]]
if __name__ == "__main__":
  N,M= map(int,input().split())
  arr = list(input() for _ in range(N))
  solution()