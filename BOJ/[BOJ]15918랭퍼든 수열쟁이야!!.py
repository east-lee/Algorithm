def DFS(k=1):
  global visited, result, cnt
  if k == n+1:
    cnt += 1
    return

  if visited[k]:
    DFS(k+1)
  else:
    for i in range(1,2*n+1):
      start = i
      end = i + k + 1
      if end >= (2*n+1): break
      elif result[start] or result[end]: continue
      else:
        result[start], result[end],visited[k] = k,k,1
        DFS(k+1)
        result[start], result[end], visited[k] = 0,0,0

if __name__ == "__main__":
  n, x, y = map(int,input().split())
  visited = [0]*(n+1)
  result = [0]*(2*n+1)
  cnt = 0

  k = y-x-1
  visited[k], result[x], result[y] = 1, k, k
  DFS()
  print(cnt)
