import sys

def DFS(index, max_num, min_num,cnt):
  global result

  if max_num - min_num >= V:
    result = min(result,cnt)
    return
  elif index == N: return

  if result <= cnt + 1: return

  if index + 1 < N:
    DFS(index + 1, max(max_num, interest[index + 1]), min(min_num, interest[index + 1]), cnt + 1)
  if index + 2 < N:
    DFS(index + 2, max(max_num, interest[index + 2]), min(min_num, interest[index + 2]), cnt + 1)

def get_data():
  N, V = map(int, input().split())

  interest = list(map(int,input().split()))

  return [N, V, interest]

if __name__ =="__main__":
  N, V, interest = get_data()

  result = sys.maxsize

  if (max(interest) - min(interest)) < V:
    print(N)
  else:
    DFS(0, interest[0], interest[0], 1)
    print(result)
