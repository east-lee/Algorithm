def floyd_warshall():
  global arr

  for k in range(1, N + 1):
    for i in range(1, N + 1):
      for j in range(1, N + 1):
        if arr[i][j]: continue

        if arr[i][k] == 1 and arr[k][j] == 1:
          arr[i][j] = 1
        elif arr[i][k] == -1 and arr[k][j] == -1:
          arr[i][j] = -1

def main():

  floyd_warshall()

  for num1, num2 in find_arr:
    print(arr[num1][num2])

def get_data():
  N, K = map(int,input().split())
  arr = [
    [0]*(N+1) for _ in range(N+1)
  ]
  find_arr = []

  for _ in range(K):
    number_1, number_2 = map(int,input().split())
    arr[number_1][number_2] = -1
    arr[number_2][number_1] = 1

  S = int(input())

  for _ in range(S):
    number_1, number_2 = map(int, input().split())
    find_arr.append([number_1, number_2])

  return [N, K, arr, find_arr]

if __name__ == "__main__":
  N, K, arr, find_arr = get_data()
  main()

