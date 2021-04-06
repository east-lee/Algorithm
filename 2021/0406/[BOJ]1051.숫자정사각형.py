if __name__ == "__main__":
  N, M = map(int,input().split())
  arr = list(list(input()) for _ in range(N))
  result = 0
  length = min(N,M)
  while length>0:
    # print(length)
    for i in range(N-length+1):
      for j in range(M-length+1):
        check_value = arr[i][j]
        # print(check_value,arr[i+length-1][j] ,arr[i][j+length-1], arr[i+length-1][j+length-1],length)
        if check_value == arr[i+length-1][j] == arr[i][j+length-1] == arr[i+length-1][j+length-1]:
          result = length
          break
      if result:
        break
    if result:break
    length -= 1
  print(result**2)
