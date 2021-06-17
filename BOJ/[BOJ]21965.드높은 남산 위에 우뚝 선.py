def main():
  result = 'YES'
  peak = -1
  status = 0

  for i in range(N-1):
    if status == 0:
      if arr[i] < arr[i+1]: continue
      elif arr[i] == arr[i+1]: return 'NO'
      status = 1
    else:
      if arr[i] <= arr[i+1]: return 'NO'
  return result

if __name__ == "__main__":
  N = int(input())
  arr = list(map(int,input().split()))
  print(main())