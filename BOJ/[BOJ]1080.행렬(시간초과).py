import sys
from collections import deque
from copy import deepcopy



def main():
  from_arr = read_matrix()
  to_arr = read_matrix()
  result = -1
  dq = deque()
  dq.append([[],from_arr,0])
  while dq:
    path, arr, cnt = dq.popleft()
    if arr == to_arr:
      result = cnt
      break
    for i in range(N-2):
      for j in range(M-2):
        if [i,j] not in path and arr[i][j] != to_arr[i][j]:
          new_arr = deepcopy(arr)
          new_path = deepcopy(path)
          new_arr = reverse_matrix(i,j,new_arr)
          new_path.append([i,j])
          dq.append([new_path,new_arr,cnt+1])
  print(result)

def reverse_matrix(i,j,arr):
  for y in range(i,i+3):
    for x in range(j,j+3):
      arr[y][x] = '1' if arr[y][x] == '0' else '0'
  return arr

def read_matrix():
  arr = []
  for _ in range(N):
    arr.append(list(input()))
  return arr

if __name__ == "__main__":
  N, M = map(int,sys.stdin.readline().split())
  main()