def dfs(k=0, result = []):
  if k == N:
    print(" ".join(result))
    return

  for i in range(1,N+1):
    if str(i) not in result:
      dfs(k+1, result + [str(i)])

if __name__ == "__main__":
  N = int(input())
  dfs()