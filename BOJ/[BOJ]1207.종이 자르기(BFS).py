from collections import deque
from copy import deepcopy

def BFS():
  print_result = False
  dq = deque()
  result = list(['0'] * L for _ in range(L))
  dq.append([result,1])
  while dq:
    arr, cnt = dq.popleft()

    if cnt == 6:
      print_result = True
      for line in arr:
        print(''.join(line))
      break
    N, M, check_puzzle = puzzle[str(cnt)]
    for i in range(L):
      for j in range(L):
        if i + N > L or j + M > L:
          continue
        else:
          new_arr = deepcopy(arr)
          breaker = False
          for n in range(N):
            for m in range(M):
              y,x = i+n, j+m
              if check_puzzle[n][m] == '#' and new_arr[y][x] == '0':
                new_arr[y][x] = str(cnt)
              elif check_puzzle[n][m] == '#' and new_arr[y][x] != '0':
                breaker = True
                break
            if breaker: break
          if breaker:
            continue

          dq.append([new_arr,cnt+1])



  if not print_result:
    print('gg')



if __name__ == "__main__":
  L = int(input())
  puzzle = {}


  for i in range(1,6):
    N,M = map(int,input().split())
    part = list(list(input()) for _ in range(N))
    puzzle[str(i)] = [N,M,part]

  BFS()

