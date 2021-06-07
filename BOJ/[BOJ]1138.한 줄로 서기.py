def main():
  result = [-1]*(N)

  for i in range(1,N+1):
    check_cnt = arr[i-1]
    cnt = 0
    for j in range(N):
      if cnt == check_cnt and result[j] == -1:
        result[j] = i
        break
      if result[j] == -1:
        cnt += 1

  for i in result: print(i,end=' ')

if __name__ == "__main__":
  N = int(input())
  arr = list(map(int,input().split()))
  main()