def main():
  arr = [0]*(N+1)
  result = []

  for i in range(2,N+1):
    cnt = 1
    while True:
      x = i*cnt
      if x > N: break
      if arr[x] == 0:
        result.append(x)
        arr[x] = 1
      cnt += 1
  print(result[K-1])


if __name__ == "__main__":
  N, K = map(int,input().split())
  main()