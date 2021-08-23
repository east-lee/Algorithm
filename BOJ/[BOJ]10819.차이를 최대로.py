def get_data():
  N = int(input())
  arr = list(map(int,input().split()))

  return [N, arr]

def get_result():
  global max_result

  result = 0
  for i in range(N-1):
    result += abs(new_arr[i] - new_arr[i+1])

  max_result = max(max_result, result)

def dfs(k = 0):
  global visited, new_arr
  if k == N:
    get_result()
    return

  for i in range(N):
    if not visited[i]:
      visited[i] = True
      new_arr.append(arr[i])
      dfs(k+1)
      visited[i] = False
      new_arr.pop()

if __name__ == "__main__":
  N, arr = get_data()
  new_arr = []
  max_result = 0
  visited = [False] * N
  dfs()

  print(max_result)
