from copy import deepcopy

def solution():
  result = -1
  check = list([0]*M for _ in range(N))
  q, new_q = [], []

  q.append([0,0,0,1,check])
  while q:

    y,x,broken,cnt,check = q.pop()
    if y == N-1 and x == M-1:
      result = cnt
      break
    for k in range(4):
      i,j = y+direction[k][0], x+direction[k][1]
      if 0<=i<N and 0<=j<M:
        new_check = deepcopy(check)
        if arr[i][j] == '1' and not broken and not new_check[i][j]:
          new_check[i][j] = 1
          new_q.append([i,j,1,cnt+1,new_check])
        elif arr[i][j] == '0' and not new_check[i][j]:
          new_check[i][j] =1
          new_q.append([i,j,broken,cnt+1,new_check])
    if not q and new_q:
      q = new_q
      new_q = []
  print(result)


direction = [[1,0],[0,1],[-1,0],[0,-1]]
if __name__ == "__main__":
  N,M= map(int,input().split())
  arr = list(input() for _ in range(N))
  solution()