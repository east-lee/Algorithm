import copy

def main():
  arr = list(input() for _ in range(N))
  # for i in arr:print(i)
  q, new_q =[], []
  check_dict = {}
  check_dict[arr[0][0]] = 1
  q.append([0,0,check_dict])
  result = 0
  while q:
    y,x,check = q.pop()
    result = len(check)
    for k in range(4):
      i,j = y+direction[k][0], x+direction[k][1]
      # print(len(check),arr[i][j],check,y,x)
      if 0<=i<N and 0<=j<M and arr[i][j] not in check.keys():
        # print('pass',check.keys())
        new_check = copy.deepcopy(check)
        new_check[arr[i][j]] = 1
        new_q.append([i,j,new_check])

    if not q and new_q:
      print(new_q)
      q = new_q
      new_q = []

  return result

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

if __name__ == "__main__":
  N, M = map(int,input().split())
  print(main())