import math
def main():
  result = -1
  for i in range(N):
    for j in range(M):
      for m in range(-M,M):
        for n in range(-N,N):
          if not m and not n:continue
          start_i, start_j = i,j
          check_num = ''
          while 0<=start_i<N and 0<=start_j<M:
            check_num += arr[start_i][start_j]
            num = int(check_num)
            num_sqrt = math.sqrt(num)
            if int(num_sqrt) == num_sqrt:
              result = max(result,num)
            start_i += n
            start_j += m
  print(result)


if __name__ == "__main__":
  N,M = map(int,input().split())
  arr = list(list(input()) for _ in range(N))

  if N==0 and M == 0:
    print(-1)
  else:
    main()