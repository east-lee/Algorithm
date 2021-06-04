def dfs(k=0,sum_result=0,cnt=0,last_idx=-1):
  global result
  if sum_result == S and cnt:
    result += 1
  if k == N:
    return

  for i in range(last_idx+1,N):
    dfs(k+1,sum_result+arr[i],cnt+1,i)

if __name__ == "__main__":
  N, S = map(int,input().split())
  arr = list(map(int,input().split()))
  result = 0
  dfs()
  print(result)