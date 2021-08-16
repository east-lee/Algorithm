from collections import deque

def bfs():
  q = deque()

  q.append(a)
  visited = [-1] * N
  visited[a] = 0

  while q:
    point = q.popleft()
    if point == b:
      return visited[point]
    for i in range(N):
      if (i-point)%arr[point] or visited[i] != -1: continue

      q.append(i)
      visited[i] = visited[point] + 1

  return -1

def get_data():
  #징검다리의 개수
  N = int(input())
  arr = list(map(int, input().split()))
  a, b = map(int, input().split())

  return [N, arr, a - 1 , b - 1]

if __name__ == "__main__":
  N, arr, a, b = get_data()
  print(bfs())
