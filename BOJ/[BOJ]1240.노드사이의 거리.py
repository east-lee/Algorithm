from collections import deque


def BFS(point_1, point_2):
  dq = deque()
  dq.append([point_1,0])
  visited = [False] * (N+1)
  visited[point_1] = True

  while dq:
    start,distance = dq.popleft()

    if start == point_2:
      return distance

    for end in range(1,N+1):
      if node_link[start][end] and not visited[end]:
        dq.append([end,node_link[start][end]+distance])
        visited[end] = True


def get_data():
  N, M = map(int,input().split())
  node_link = [
    [0] * (N+1) for _ in range(N+1)
  ]

  find_node_list = []

  for _ in range(N-1):
    start, end, distance =map(int,input().split())
    node_link[start][end] = distance
    node_link[end][start] = distance

  for _ in range(M):
    point_1, point_2 = map(int,input().split())
    find_node_list.append([point_1,point_2])

  return [N,M,node_link,find_node_list]


if __name__ == "__main__":
  N, M, node_link, find_node_list = get_data()

  for point_1, point_2 in find_node_list:
    result = BFS(point_1,point_2)
    print(result)