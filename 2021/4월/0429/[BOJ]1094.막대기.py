def main():
  arr = [64]
  cnt = 0
  while sum(arr)!=X:
    cnt += 1
    if (sum(arr) > X):
      x = arr.pop()
      x1, x2 = x//2 , x//2
      if (sum(arr)+x1 >=X):
        arr.append(x1)
      else:
        arr.append(x1)
        arr.append(x2)
  print(len(arr))

if __name__ == "__main__":
  X = int(input())
  main()