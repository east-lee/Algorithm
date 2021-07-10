from collections import deque

def main(start):
  global visited

  visited[start] = 1
  q = deque()
  q.append(start)

  while q:
    point = q.popleft()
    for end_point in link_list[point]:
      if visited[end_point]  == 0:
        visited[end_point] = -visited[point]
        q.append(end_point)
      else:
        if visited[point] == visited[end_point]:
          return False
  return True

def get_data():
  V, E = map(int,input().split())
  link_list = [[] for _ in range(V + 1)]
  visited = [0 for _ in range(V+1)]

  for _ in range(E):
    s, e = map(int, input().split())
    link_list[s].append(e)
    link_list[e].append(s)

  return [V, E, link_list, visited]

if __name__ == "__main__":
  T = int(input())

  for _ in range(T):
    V, E, link_list, visited = get_data()
    result = 'YES'
    for start in range(1,V+1):
      if visited[start] == 0:
        check_result = main(start)
        if not check_result:
          result = 'NO'
          break
    print(result)