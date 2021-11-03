def get_data():
  N, B = map(int, input().split())
  matrix = list(list(map(int,input().split())) for _ in range(N))

  return [N, B, matrix]

def num_to_bin():
  global B
  result = ""
  while B:
    result += str(B%2)
    B = B//2

  return result[::-1]

def solution(matrix_1, matrix_2):
  return_matrix = [[0]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      for k in range(N):
        return_matrix[i][j] += int(matrix_1[i][k]) * int(matrix_2[k][j])
      return_matrix[i][j] = str(return_matrix[i][j] % 1000)
  return return_matrix


if __name__ == "__main__":
  N, B, matrix = get_data()
  B = num_to_bin()
  result = [[0]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      result[i][j] = 1 if i == j else 0

  for i in range(len(B)):
    if B[-i-1] == "1":
      check = matrix[:]
      while i:
        check = solution(check, check)
        i -= 1
      result = solution(result, check)

  for line in result:
    print(" ".join(line))