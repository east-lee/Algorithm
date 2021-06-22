def DFS(k=0, result = '', last_num = 1):
  if k == M:
    print(result[1:])
    return

  for i in range(last_num, N+1):
    DFS(k+1, result + ' ' + str(i), i)

if __name__ == "__main__":
  N, M = map(int,input().split())
  DFS()