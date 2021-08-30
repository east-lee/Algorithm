# 브루트포스 => 시간초과

def dfs(k=0, check_length=0, check_list = []):
  global max_list,result_list, max_length

  if check_length + N - k < max_length: return
  elif k == N:
    check_list.sort()
    if check_list == max_list and check_length > max_length:
      result_list = max_list[:]
      max_length = check_length
    return


  if not (num_list[1][k] < num_list[0][k] and num_list[1][k] not in max_list):
    max_list.append(num_list[0][k])
    dfs(k+1, check_length + 1, check_list + [num_list[1][k]])
    max_list.pop()
  if num_list[0][k] not in check_list:
    dfs(k + 1, check_length, check_list)




def get_data():
  N = int(input())
  num_list = [
    [i for i in range(1,N+1)],
    [int(input()) for _ in range(N)]
  ]

  return [N, num_list]

if __name__ == "__main__":
  N, num_list = get_data()
  max_length = 0
  max_list = []
  result_list = []
  dfs()


  print(max_length)
  for num in result_list: print(num)