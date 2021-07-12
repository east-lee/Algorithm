def DFS(k=0, sum_caffeine = 0, cnt = 0):
  global result

  if result != -1 and cnt > result:
    return

  if k == N:
    if sum_caffeine == K:
      if result == -1: result = cnt
      else: result = min(result, cnt)
    return
  if sum_caffeine == K:
    if result == -1:
      result = cnt
    else:
      result = min(result, cnt)
    return

  DFS(k + 1, sum_caffeine+caffeine[k], cnt+1)
  DFS(k + 1, sum_caffeine, cnt)


def get_data():
  N, K = map(int,input().split())
  caffeine = list(map(int,input().split()))

  return [N, K, caffeine]


if __name__ == "__main__":
  N, K, caffeine = get_data()
  result = -1
  DFS()
  print(result)