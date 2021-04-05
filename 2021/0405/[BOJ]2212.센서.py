def main():
  distance = []
  for i in range(N-1):
    distance.append(arr[i+1]-arr[i])

  distance.sort()
  for _ in range(K-1): distance.pop()

  print(sum(distance))


if __name__ == "__main__":
  N = int(input())
  K = int(input())
  arr = list(map(int,input().split()))
  arr.sort()
  if K >= N:
    print(0)
  else:
    main()