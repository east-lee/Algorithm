def main():
  result = [0] * N
  mid_num = N//2 if N%2==1 else N//2-1
  for i in range(1,N-1):
    if i <= mid_num: result[i] = i
    else: result[i] = i+2
  result[0] = mid_num + 1
  result[N-1] = mid_num+ 2

  for r in result: print(r)
  
if __name__ == "__main__":
  N = int(input())
  if N <= 3:
    print(-1)
  else:
    main()