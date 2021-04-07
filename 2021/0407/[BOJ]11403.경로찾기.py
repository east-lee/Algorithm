if __name__ == "__main__":
  N = int(input())
  arr = list(list(map(int,input().split())) for _ in range(N))
  for k in range(N):
    for i in range(N):
      for j in range(N):
        if arr[i][j] or (arr[i][k] and arr[k][j]):
          arr[i][j] = 1
  for i in arr:
    for j in i:
      print(j,end=' ')
    print()