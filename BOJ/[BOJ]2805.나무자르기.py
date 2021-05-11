if __name__ == "__main__":
  N,M = map(int,input().split())
  trees = list(map(int,input().split()))

  start, end = 0,max(trees)
  result = 0

  while start <= end:
    mid = (start+end)//2

    cnt = 0
    for tree in trees:
      if tree-mid >=0: cnt += (tree-mid)

    if cnt >= M:
      start = mid+1
      result = mid
    else: end = mid-1
  print(result)
