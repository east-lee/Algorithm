import sys, heapq

def get_data():
  N, M, X = map(int, input().split())
  road = [
    [] for _ in range(N+1)
  ]

  for _ in range(M):
    s, e, t = map(int ,input().split())
    road[s].append((e,t))

  return [N, M, X, road]

def dijkstra(start_node, end_node):
  distance = [INF] * (N+1)
  q = []
  heapq.heappush(q, (0, start_node))
  distance[start_node] = 0

  while q:
    d, node = heapq.heappop(q)

    if distance[node] < d: continue

    for idx, time in road[node]:
      total_time = d + time
      if distance[idx] > total_time:
        distance[idx] = total_time
        heapq.heappush(q, (total_time, idx))


  return distance[end_node]

if __name__ == "__main__":
  N, M, X, road = get_data()
  INF = sys.maxsize
  result = 0

  for i in range(1,N+1):
    if X == i: continue

    result = max(result, dijkstra(i,X) + dijkstra(X,i))

  print(result)

