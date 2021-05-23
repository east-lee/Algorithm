def main():
  count = 0
  visited = list([0]*M for _ in range(N))
  visited[start_i][start_j] = 1

  q = []
  q.append([start_i,start_j])
  while q:
    y, x = q.pop()
    if campus[y][x] == 'P': count+=1
    for k in range(4):
      i,j = y+direction[k][0], x+direction[k][1]
      if 0<=i<N and 0<=j<M and campus[i][j] !='X' and visited[i][j] != 1:
        visited[i][j] = 1
        q.append([i,j])

  return count



def find_me():
  breaker = False
  for i in range(N):
    for j in range(M):
      if campus[i][j] == 'I':
        breaker = True
        break
    if breaker: break

  return [i,j]


if __name__ == "__main__":
  N, M = map(int,input().split())
  campus = list(list(input()) for _ in range(N))
  direction = [[-1,0],[1,0],[0,-1],[0,1]]
  start_i, start_j = find_me()

  result = main()
  print(result if result != 0 else 'TT')