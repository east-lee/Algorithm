def dfs(k=0, sum_check = 0, multi=1,last_num = 0):
  global sum_list,result
  if k == K:
    if sum_check == S:
      result = max(result,multi)
    return

  for i in range(1,S+1):
    if k == K-1:
      c = S-sum_check
      if c == 0:
        break
      dfs(k+1,sum_check + c,multi*c,last_num)
      break
    if last_num > i: continue
    if sum_check + i <= S:
      dfs(k+1,sum_check+i,multi*i,i)

if __name__ == "__main__":
  S, K = map(int,input().split())
  sum_list = []
  result = 0
  dfs()
  print(result)

