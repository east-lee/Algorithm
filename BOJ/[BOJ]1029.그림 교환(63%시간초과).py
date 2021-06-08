def dfs(price,cnt,last_idx):
  global visited,max_result

  next_pos = False
  for i in range(N):
    if visited[i]: continue
    i_cost = cost[last_idx][i]
    if i_cost >= price:
      next_pos = True
      visited[i] = 1
      dfs(i_cost,cnt+1,i)
  if not next_pos:
    max_result = max(max_result,cnt)


if __name__ == "__main__":
  N = int(input())
  visited = [0]*N
  cost = list(list(map(int,list(input()))) for _ in range(N))
  visited[0] = 1
  price = 0
  max_result = 0
  dfs(price,1,0)
  print(max_result)