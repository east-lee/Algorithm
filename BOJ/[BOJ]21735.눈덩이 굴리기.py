def dfs(k=0,size=1,now_position = 0):
  global result
  if k == M or now_position == N:
    result = max(result,size)
    return
  a1 = now_position + 1
  a2 = now_position + 2
  if now_position == N-1:
    dfs(k + 1, size + arr[a1], a1)
  else:
    dfs(k + 1, size + arr[a1], a1)
    dfs(k + 1, size // 2 + arr[a2], a2)


if __name__ == "__main__":
  N, M = map(int,input().split())
  arr = list(map(int,input().split()))
  arr.insert(0,0)
  result = 0
  dfs()
  print(result)