def main():
  result = []
  for i in range(L,101):
    if i % 2 == 0 and N%i == 0.5:
      for left in range(N//i+1-i//2,N//i+1):
        result.append(left)
      for right in range(N//i+1,N//i+1+i//2):
        result.append(right)
    elif i % 2 == 1 and N%i == 0:
      for right in range(N//i-i//2,N//i):
        result.append(right)
      for left in range(N//i,N//i+i//2+1):
        result.append(left)
    if -1 in result: result = []
    if result:
      break
  if result:
    for i in result: print(i,end=' ')
    print()
  else:print(-1)


if __name__ == "__main__":
  N, L = map(int,input().split())
  main()