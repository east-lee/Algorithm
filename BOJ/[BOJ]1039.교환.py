from copy import deepcopy

def dfs(k,dfs_result,n,last_idx):
  global result
  if dfs_result[0] == '0': return
  if k == K:
    num = ''.join(dfs_result)
    if result < int(num): result = int(num)
    return

  for i in range(n):
    for j in range(i+1,n):
      copy_result = deepcopy(dfs_result)
      copy_result[i],copy_result[j] = copy_result[j], copy_result[i]
      dfs(k+1,copy_result,n,i)

def main():
  global N
  N = list(str(N))
  dfs(0,N,len(N),0)

if __name__ == "__main__":
  N, K = map(int,input().split())
  result = -1
  main()
  print(result)