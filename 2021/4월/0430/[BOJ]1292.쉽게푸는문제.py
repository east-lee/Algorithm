if __name__ == "__main__":
  a,b = map(int,input().split())
  arr = []
  for i in range(1001):
    for j in range(i):
      arr.append(i)
    if len(arr)>1000: break
  print(sum(arr[a-1:b]))
