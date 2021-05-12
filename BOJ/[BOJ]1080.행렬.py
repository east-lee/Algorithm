import sys

def main():
  global from_arr
  cnt = 0
  for i in range(N-2):
    for j in range(M-2):
      if from_arr[i][j] != to_arr[i][j]:
        from_arr = reverse_matrix(i,j,from_arr)
        cnt += 1
  for i in range(N):
    for j in range(M):
      if from_arr[i][j] != to_arr[i][j]: return -1
  return cnt


def reverse_matrix(y,x,arr):
  for i in range(y,y+3):
    for j in range(x,x+3):
      arr[i][j] = 1 if arr[i][j] == 0 else 0
  return from_arr


if __name__ == "__main__":
  N, M = map(int,sys.stdin.readline().split())
  from_arr = list(list(map(int,list(input()))) for _ in range(N))
  to_arr = list(list(map(int,list(input()))) for _ in range(N))
  print(main())