def main():
  dfs()

def dfs(n=0,y=0,x=0):
  global cnt
  if n == N:
    cnt += 1
    if y == r and x == c: print(cnt)
    return

  length = 2**(N-n-1)
  dfs(n+1,y,x)
  dfs(n+1,y,x+length)
  dfs(n+1,y+length,x)
  dfs(n + 1, y + length, x + length)


if __name__ == "__main__":
  N, r,c = map(int,input().split())
  cnt = -1
  main()