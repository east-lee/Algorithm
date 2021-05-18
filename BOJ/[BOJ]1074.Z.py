def main():
  dfs()


def dfs(n=0, y=0, x=0, total_cnt = 0):
  global cnt
  if n == N:
    cnt += 1
    if y == r and x == c: print(cnt+total_cnt)
    return

  length = 2 ** (N - n - 1)
  if y <= r < y+length and x<=c<x+length:
    dfs(n + 1, y, x, total_cnt)
  elif y <= r < y+length and x+length<=c<x+2*length:
    dfs(n + 1, y, x + length ,total_cnt +  length**2)
  elif y+length <= r <y+2*length and x<=c<x+length:
    dfs(n + 1, y + length, x,total_cnt + 2*(length**2) )
  else:
    dfs(n + 1, y + length, x + length,total_cnt + 3*(length**2) )


if __name__ == "__main__":
  N, r, c = map(int, input().split())
  cnt = -1
  main()