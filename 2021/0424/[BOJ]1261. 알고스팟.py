from collections import deque

def BFS():
  global result
  q = deque()
  visited = [[-1]*N for _ in range(M)]
  visited[0][0] = 0
  q.append([0,0])
  while q:
    y,x = q.popleft()
    for k in range(4):
      i,j = y+direction[k][0], x+direction[k][1]
      if 0<=i<M and 0<=j<N and visited[i][j] == -1:
        if maze[i][j] == '1':
          q.append([i,j])
          visited[i][j] = visited[y][x]+1
        else:
          q.appendleft([i,j])
          visited[i][j] = visited[y][x]
  print(visited[M-1][N-1])





direction = [[-1,0],[1,0],[0,1],[0,-1]]

if __name__ == "__main__":
  N,M = map(int,input().split())
  maze = list(input() for _ in range(M))

  result = list([100000]*N for _ in range(M))
  result[0][0] = 0

  BFS()