def dfs(matrix, k):
  if k == s:
    return matrix

  matrix_length = N**(k+1)
  new_matrix = list([0]*(matrix_length) for _ in range(matrix_length))

  for i in range(len(matrix)):
    for j in range(len(matrix)):
      convert_matrix = one_convert_to if matrix[i][j] else zero_convert_to
      start_i = N*i
      start_j = N*j
      for m in range(N):
        for n in range(N):
          new_matrix[start_i+m][start_j+n] = convert_matrix[m][n]
  return dfs(new_matrix, k+1)



def main():
  first_matrix = [[0]]
  return dfs(first_matrix,0)


if __name__ == "__main__":
  s,N,K,R1,R2,C1,C2 = map(int,input().split())

  one_convert_to = list([1]*N for _ in range(N))
  zero_convert_to = list([0]*N for _ in range(N))
  start_point = (N-K)//2

  for i in range(start_point,start_point+K):
    for j in range(start_point,start_point+K):
      zero_convert_to[i][j] = 1

  result_matrix = main()

  for i in range(R1,R2+1):
    for j in range(C1,C2+1):
      print(result_matrix[i][j],end='')
    print()
