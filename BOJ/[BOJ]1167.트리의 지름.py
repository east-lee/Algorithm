from collections import deque

def solution(v):

  visited = [False] * (V + 1)
  q = deque()
  q.append([v,0])

  result_dist = 0
  result_node = -1

  while q:
    from_node, dist = q.popleft()
    visited[from_node] = True
    if result_dist < dist:
      result_node = from_node
      result_dist = dist

    for to_node, next_dist in link_list[from_node]:
      if visited[to_node]: continue
      q.append([to_node, dist+next_dist])

  return [result_dist, result_node]



def get_data():
  V = int(input())
  link_list = [[] for _ in range(V+1)]

  for _ in range(V):
    info = list(map(int, input().split()))
    v_num = info[0]
    info = info[1:-1]

    for i in range(len(info)//2):
      to_num, dist = info[2*i], info[2*i+1]
      link_list[v_num].append([to_num, dist])

  return [V, link_list]


if __name__ == "__main__":
  V, link_list = get_data()
  result, node = solution(1)
  result, _ = solution(node)

  print(result)
