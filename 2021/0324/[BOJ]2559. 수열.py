def main():
  result = -1000000000000000000
  check = 0
  for i in range(n-k+1):
    if i == 0:
      check = sum(arr[:k])
    else:
      check = check + arr[i+k-1] - arr[i-1]
    result = max(result,check)

  print(result)


if __name__ == "__main__":
  n, k = map(int,input().split())
  arr = list(map(int,input().split()))
  main()