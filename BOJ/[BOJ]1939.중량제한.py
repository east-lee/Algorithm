from collections import deque
import sys

def get_data():
  N, M = map(int,input().split())
  arr = [
    [] for _ in range(N)
  ]

  for _ in range(M):
    s, e, c = map(int,input().split())
    s, e = s-1, e-1
    arr[s].append([e, c])
    arr[e].append([s,c])

  start, end = map(int, input().split())

  return [N, M, arr, start, end]


def BFS(check_cost):
  dq = deque()
  dq.append(start - 1)
  visited = []

  while dq:
    start_point = dq.popleft()
    if end - 1 == start_point:
      return True
    for end_point, cost in arr[start_point]:
      if end_point not in visited and cost >= check_cost:
        visited.append(end_point)
        dq.append(end_point)
  return False


if __name__ == "__main__":
  N, M, arr, start, end = get_data()
  min_cost, max_cost = 1, 1000000000
  result = min_cost

  while min_cost <= max_cost:
    mid_cost = (min_cost + max_cost) // 2

    if BFS(mid_cost):
      result = mid_cost
      min_cost = mid_cost + 1
    else:
      max_cost = mid_cost - 1

  print(result)
