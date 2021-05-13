#50점
from collections import deque


def solution(values, edges, queries):
  answer = []

  nodes = [0] + values[:]
  sum_nodes = [0] * (len(nodes))

  check = list([] for _ in range(len(nodes)))
  for s, e in edges:
    check[s].append(e)
    check[e].append(s)

  parent_node, child_node, have_child = find_parent(check)

      for i in range(1, len(nodes)):
          x = i
          while x != 0:
              sum_nodes[x] += nodes[i]
              x = parent_node[x]
  # sum_nodes = find_sum_arrs(parent_node, child_node, have_child, nodes)

  for u, w in queries:
    if w == -1:
      answer.append(sum_nodes[u])
    else:
      nodes, sum_nodes = change_node(u, w, parent_node, sum_nodes, nodes)
  return answer


def find_sum_arrs(parent_node, child_node, have_child, nodes):
  dq = deque()

  arr = [0] * (len(nodes))
  print(child_node)
  for i in range(1, len(nodes)):
    if not have_child[i]: dq.append(i)

  check_child = [0] * len(nodes)
  while dq:
    x = dq.popleft()
    p_x = parent_node[x]
    if len(child_node[x]) != check_child[x]: continue
    arr[x] = nodes[x]
    for y in child_node[x]:
      arr[x] += arr[y]
    check_child[p_x] += 1
    dq.append(p_x)
  print(arr, check_child)
  return arr


def change_node(u, w, parent_node, sum_nodes, nodes):
  x = u
  lost_value = nodes[u]

  while x != 1:
    p_x = parent_node[x]
    sum_nodes[x] -= lost_value
    sum_nodes[x] += nodes[p_x]
    nodes[x] = nodes[p_x]
    x = p_x
  sum_nodes[1] = sum_nodes[1] - lost_value + w
  nodes[1] = w
  return [nodes, sum_nodes]


def find_parent(check):
  arr = [0] * len(check)
  arr2 = [[] for _ in range(len(check))]
  arr3 = [0] * len(check)
  dq = deque()
  dq.append(1)
  visited = [0] * len(check)
  visited[1] = 1
  while dq:
    x = dq.popleft()
    for i in check[x]:
      if visited[i]: continue
      arr3[x] = 1
      visited[i] = 1
      arr[i] = x
      arr2[x].append(i)
      dq.append(i)
  return [arr, arr2, arr3]


# 25점짜리
def solution(values, edges, queries):
  answer = []

  nodes = [0] + values[:]
  sum_nodes = [0] * (len(nodes))

  parent_node = [0] * (len(nodes))
  parent_node[0] = -1

  check_route = list([0] * (len(nodes)) for _ in range(len(nodes)))

  for s, e in edges:
    check_route[s][e] = 1
    check_route[e][s] = 1

  parent_node = find_route(check_route)

  for i in range(1, len(nodes)):
    q = [i]
    while q:
      x = q.pop()
      sum_nodes[x] += nodes[i]
      if parent_node[x] == 0: break
      q.append(parent_node[x])

  for u, w in queries:
    if w == -1:
      answer.append(sum_nodes[u])
    else:
      nodes, sum_nodes = change_node(u, w, parent_node, sum_nodes, nodes)
  # print(answer)
  return answer


def change_node(u, w, parent_node, sum_nodes, nodes):
  x = u
  lost_value = nodes[u]

  while x != 1:
    p_x = parent_node[x]
    sum_nodes[x] -= lost_value
    sum_nodes[x] += nodes[p_x]
    nodes[x] = nodes[p_x]
    x = p_x
  sum_nodes[1] = sum_nodes[1] - lost_value + w
  nodes[1] = w
  return [nodes, sum_nodes]


def find_route(arr):
  start = 1
  new_arr = [0] * (len(arr))
  visited = [0] * (len(arr))
  q = [1]
  visited[1] = 1
  new_q = []
  while q:
    x = q.pop()
    for i in range(len(arr)):
      if arr[x][i] == 1 and not visited[i]:
        visited[i] = 1
        new_q.append(i)
        new_arr[i] = x
    if not q and new_q:
      q = new_q
      new_q = []
  # print(new_arr)
  return new_arr


values = [1,10,100,1000,10000]
edges=[[1,2],[1,3],[2,4],[2,5]]
queries = [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]
solution(values,edges,queries)








# 4번 시간초과
# def solution(values, edges, queries):
#   answer = []
#   N = len(values)
#   nodes = values[:]
#   nodes.insert(0, 0)
#
#   child_node = list([] for _ in range(N + 1))
#   parent_node = [0] * (N + 1)
#
#   for s, e in edges:
#     child_node[s].append(e)
#     parent_node[e] = s
#
#   for u, w in queries:
#     if w == -1:
#       answer.append(solution_1(u, child_node, N, nodes))
#     else:
#       nodes = solution_2(u, w, nodes, parent_node)
#
#   return answer
#
#
# def solution_2(u, w, nodes, parent_node):
#   q = []
#   q.append(u)
#
#   while q:
#     x = q.pop()
#     if x == 1:
#       nodes[1] = w
#       break
#     nodes[x] = nodes[parent_node[x]]
#     q.append(parent_node[x])
#   # print(nodes)
#   return nodes
#
#
# def solution_1(start_point, node, N, nodes):
#   q = []
#   visited = [0] * (N + 1)
#   result = 0
#   q.append(start_point)
#
#   while q:
#     x = q.pop()
#     if visited[x]: continue
#     visited[x] = 1
#     result += nodes[x]
#     q.extend(node[x])
#   return result


# from collections import deque
#
#
# def solution(values, edges, queries):
#   answer = []
#   N = len(values)
#
#   nodes = [0] + values[:]
#
#   child_node = list([] for _ in range(N + 1))
#   parent_node = [0] * (N + 1)
#
#   visited_check = [0] * (N + 1)
#
#   for s, e in edges:
#     child_node[s].append(e)
#     parent_node[e] = s
#     visited_check[s] = 1
#
#   dq = deque()
#   for i in range(1, N + 1):
#     if not visited_check[i]: dq.append(i)
#
#   child_cnt_check = [0] * (N + 1)
#   sum_nodes = [0] * (N + 1)
#
#   while dq:
#     x = dq.popleft()
#     parent_idx = parent_node[x]
#     if len(child_node[x]) != child_cnt_check[x]: continue
#
#     sum_nodes[x] += nodes[x]
#     for y in child_node[x]:
#       sum_nodes[x] += sum_nodes[y]
#
#     child_cnt_check[parent_idx] += 1
#     dq.append(parent_idx)
#
#   print(sum_nodes)
#
#   return answer
#
#
# from collections import deque
#
#


# 4번 시간초과
# def solution(values, edges, queries):
#   answer = []
#   N = len(values)
#
#   nodes = [0] + values[:]
#
#   child_node = list([] for _ in range(N + 1))
#   parent_node = [0] * (N + 1)
#
#   visited_check = [0] * (N + 1)
#
#   for s, e in edges:
#     child_node[s].append(e)
#     parent_node[e] = s
#     visited_check[s] = 1
#
#   dq = deque()
#   for i in range(1, N + 1):
#     if not visited_check[i]: dq.append(i)
#
#   child_cnt_check = [0] * (N + 1)
#   sum_nodes = [0] * (N + 1)
#   visited = [0] * (N + 1)
#   while dq:
#     x = dq.popleft()
#     parent_idx = parent_node[x]
#     if len(child_node[x]) != child_cnt_check[x] or visited[x]: continue
#     sum_nodes[x] += nodes[x]
#     visited[x] = 1
#     for y in child_node[x]:
#       sum_nodes[x] += sum_nodes[y]
#
#     child_cnt_check[parent_idx] += 1
#     dq.append(parent_idx)
#
#   for u, w in queries:
#     if w == -1:
#       answer.append(sum_nodes[u])
#     else:
#       nodes, sum_nodes = change_node(u, w, nodes, parent_node, sum_nodes)
#   print(answer)
#   return answer
#
#
# def change_node(u, w, nodes, parent_node, sum_nodes):
#   x = u
#   first_value = nodes[x]
#   while x != 1:
#     p_x = parent_node[x]
#     sum_nodes[x] = sum_nodes[x] - nodes[x] + nodes[p_x]
#     if x != u:
#       sum_nodes[x] -= first_value - nodes[x]
#     nodes[x] = nodes[p_x]
#     x = p_x
#   sum_nodes[1] = sum_nodes[1] - nodes[1] + w - first_value + nodes[x]
#   nodes[1] = w
#   # print(nodes,sum_nodes)
#   return [nodes, sum_nodes]