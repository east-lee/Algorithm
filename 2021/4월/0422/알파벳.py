import copy


def main():
  arr = list(list(map(lambda x:ord(x)-65,input())) for _ in range(N))
  check = [False]*26
  q, next_q = list(list() for _ in range(2))
  check[arr[0][0]] = True
  q.append([0,0,check,1])
  result = 0
  while q:
    y,x,c,cnt = q.pop()
    for k in range(4):
      i,j = y+direction[k][0], x+direction[k][1]
      if 0<=i<N and 0<=j<M and not c[arr[i][j]]:
        new_check = copy.deepcopy(c)
        new_check[arr[i][j]] = True
        next_q.append([i,j,new_check,cnt+1])
        result = max(cnt+1,result)

    if not q and next_q:
      q = next_q
      next_q = []

  return result

direction = [[-1,0], [1,0], [0,-1], [0,1]]

if __name__ == "__main__":
  N, M = map(int,input().split())
  print(main())