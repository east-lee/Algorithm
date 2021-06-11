if __name__ == "__main__":
  N, M, K = map(int,input().split())

  arr = list([0]*M for _ in range(N))
  visited = list([0]*M for _ in range(N))
  direction = [[-1,0],[1,0],[0,-1],[0,1]]
  result = 0

  for _ in range(K):
    y, x = map(int,input().split())
    y, x = y-1, x-1
    arr[y][x] = '#'

  for i in range(N):
    for j in range(M):
      if arr[i][j] == '#' and not visited[i][j]:
        q = [[i,j]]
        cnt = 0
        while q:

          y,x = q.pop()
          if visited[y][x]: continue
          visited[y][x] = 1
          cnt += 1

          for k in range(4):
            next_y, next_x = y+direction[k][0], x+direction[k][1]

            if 0<=next_y<N and 0<=next_x<M and arr[next_y][next_x] == '#':
              q.append([next_y,next_x])

        result = max(result,cnt)

  print(result)