def find_min_cost(arr):

  min_cost = 1000001

  for i in arr:
    min_cost = min(min_cost, cost[i])

  return min_cost


def make_group(start):
  global visited


  group = [start]

  for i in range(N):
    if i == start and visited[i] == True: continue

    if roads[start][i] == 1 and roads[start][i] == roads[i][start]:
      visited[i] = True
      group.append(i)
  return find_min_cost(group)



def custom_graph(start,first):
  global roads, visited

  for i in range(N):
    if i == start or visited[i] == True or roads[start][i] == 0: continue
    
    visited[i] = True
    roads[first][i] = 1
    custom_graph(i, first)    


def get_data():
  N = int(input())  # 도시의 개수
  cost = list(map(int, input().split()))  # 도시별 경찰서 건축 비용
  roads = list(
      list(map(int, input())) for _ in range(N)
  )

  return [N, cost, roads]


if __name__ == "__main__":
  N, cost, roads = get_data()


  for i in range(N):
    visited = [False] * N
    custom_graph(i,i)
  
  # for road in roads: print(road)

  result = 0

  visited = [False] * N
  for i in range(N):
    if visited[i]: continue
    result += make_group(i)

  print(result)