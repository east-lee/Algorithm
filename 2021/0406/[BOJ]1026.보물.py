if __name__ == "__main__":
  N = int(input())
  A,B = [list(map(int,input().split())) for _ in range(2)]
  A.sort()
  visited = [False for _ in range(N)]
  result = 0

  for i in range(N):
    max_result = 0
    max_jdx = -1
    for j in range(N):
      if not visited[j] and max_result < B[j]:
        max_result = B[j]
        max_jdx = j

    visited[max_jdx]=True
    result += A[i]*max_result
  print(result)


