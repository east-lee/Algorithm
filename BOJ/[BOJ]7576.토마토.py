from collections import deque

direction = [[-1,0],[1,0],[0,-1],[0,1]]

result = 0
def main():
  tomatoes = list(list(map(int, input().split())) for _ in range(N))
  total_tomato = N*M
  finish_tomato = 0
  dq = deque()
  for i in range(N):
    for j in range(M):
      if tomatoes[i][j] == 1:
        dq.append([i,j,0])
      elif tomatoes[i][j] == -1: total_tomato -= 1


  while dq:
    y, x, cnt = dq.popleft()
    result = cnt
    finish_tomato += 1

    for k in range(4):
      i ,j = y+ direction[k][0] , x + direction[k][1]
      if 0<=i<N and 0<=j<M and tomatoes[i][j] == 0:
        tomatoes[i][j] = 1
        dq.append([i,j,cnt+1])

  if finish_tomato != total_tomato: print(-1)
  else:print(result)

if __name__ == "__main__":
  M, N = map(int,input().split())
  main()