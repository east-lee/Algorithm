def dfs(k,y,x,cnt ):
  global visited, arr, result
  if k == T:
    result = max(result,cnt)
    return

  dfs(k+1,y,x,cnt)

  for m in range(4):
    i, j = y+direction[m][0], x+direction[m][1]
    if 0<=i<R and 0<=j<C and not visited[i][j] and arr[i][j] != '#':
      visited[i][j] = 1
      if arr[i][j] == 'S':
        arr[i][j] = '.'
        dfs(k+1,i,j,cnt+1)
        arr[i][j] = 'S'
      else:
        dfs(k+1,i,j,cnt)
      visited[i][j] = 0


if __name__ == "__main__":
  direction = [[-1,0],[1,0],[0,-1],[0,1]]

  R,C,T = map(int,input().split())
  visited = list([0] * C for _ in range(R))
  arr = list(list(input()) for _ in range(R))
  start_i, start_j = 0,0
  breaker = False
  for i in range(R):
    for j in range(C):
      if arr[i][j] == 'G':
        start_i, start_j = i, j
        breaker = True
        break
    if breaker: break
  result = 0
  dfs(0,start_i, start_j,0)
  print(result)
