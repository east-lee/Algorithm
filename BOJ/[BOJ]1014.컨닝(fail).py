def max_pos(y,x):
  cnt = 0
  for i in range(y+1,N):
    for j in range(M):
       if desk[i][j] == '.':
         cnt += 1
  for j in range(x,M):
    if desk[y][j] == '.': cnt+=1
  return cnt

def DFS(y,x,cnt):
  global desk,max_student
  x = x+1 if x+1 < M else 0
  y = y if x != 0 else y+1

  if y==N:
    max_student = max(max_student,cnt)
    return

  if cnt + max_pos(y,x)//2 < max_student:
    return

  if desk[y][x] == '.':
    return_desk = []
    for k in range(5):
      i,j = y+cant_sit[k][0], x+cant_sit[k][1]
      if 0<=i<N and 0<=j<M and desk[i][j] == '.':
        return_desk.append([i,j])
        desk[i][j] = 'x'
    DFS(y,x,cnt+1)
    for i,j in return_desk:
      desk[i][j] = '.'
  DFS(y,x,cnt)




def main():
  DFS(-1,M,0)


if __name__ ==  "__main__":
  C = int(input())
  cant_sit = [[0,0],[0,1],[0,-1],[1,1],[1,-1]]
  for _ in range(C):
    N, M = map(int, input().split())
    desk = list(list(input()) for _ in range(N))
    max_student = 0
    main()
    print(max_student)