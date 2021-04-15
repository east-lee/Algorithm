if __name__ == "__main__":
  N, M = map(int,input().split())
  arr = list(list(input()) for _ in range(N))

  q = [[0,0,arr[0][0]]]
  new_q = []
  direction = [[-1,0],[1,0],[0,1],[0,-1]]
  result = 0

  while q:
    y,x,path = q.pop()
    if len(path) > result:result=len(path)
    for k in range(4):
      i,j = y+direction[k][0], x+direction[k][1]
      if 0<=i<N and 0<=j<M and arr[i][j] not in path:
        new_q.append([i,j,path+arr[i][j]])
    if not q and new_q:
      q = new_q
      new_q = []

  print(result)
  

