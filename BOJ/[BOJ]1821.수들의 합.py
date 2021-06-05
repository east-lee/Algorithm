def find_sum(arr):
  for i in range(N):
    virtual_tree[0][i] = arr[i]

  depth = 1
  while depth < N:
    for i in range(N-1):
      virtual_tree[depth][i] = virtual_tree[depth-1][i] + virtual_tree[depth-1][i+1]
    depth += 1

  if virtual_tree[N-1][0] == F:
    return True
  return False



def find_combination(k=0,cb = []):
  global combination_list, final_result
  if final_result: return
  if k == N:
    if find_sum(cb):
      final_result = cb[:]
    return
  for i in range(1,N+1):
    if combination_list[i] == 1:
      continue
    combination_list[i] = 1
    find_combination(k+1,cb+[i])
    combination_list[i] = 0


if __name__ == "__main__":
  N, F = map(int,input().split())
  virtual_tree = list([0]*N for _ in range(N))
  combination_list = [0]*(N+1)
  final_result = []
  find_combination()

  for i in final_result:
    print(i,end=' ')