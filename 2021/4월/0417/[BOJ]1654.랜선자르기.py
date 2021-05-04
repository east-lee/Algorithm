if __name__ == "__main__":
  N, K = map(int,input().split())
  arr = []
  for _ in range(N):arr.append(int(input()))

  left,right = 1,max(arr)
  result =0
  while left <= right:
    mid = (left+right)//2

    cnt = 0
    for i in arr:
      cnt += i//mid

    if cnt >= K:
      left = mid+1
      result = mid
    else: right = mid-1
  print(result)



