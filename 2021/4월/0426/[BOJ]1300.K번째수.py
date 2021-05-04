def main():
  left,right = 1, K
  result = 0
  while left <= right:
    mid = (left+right) // 2

    cnt = 0

    for i in range(1,N+1):
      cnt += mid//i if (mid//i <= N) else N
    if cnt >= K:
      result = mid
      right = mid-1
    else: left = mid+1
  print(result)


if __name__ == "__main__":
  N, K = (int(input()) for _ in range(2))
  main()
