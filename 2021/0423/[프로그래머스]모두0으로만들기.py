import sys
sys.setrecursionlimit(100000000)
answer = 0
visited = []
border = []

def solution(a, edges):
  global answer,visited, border
  answer = 0 if sum(a) == 0 else -1
  if answer < 0: return answer

  visited = [[] for _ in range(len(a))]
  border = [[] for _ in range(len(a))]

  for node1, node2 in edges:
    border[node1].append(node2)
    border[node2].append(node1)

  dfs(0,a)

  return answer

def dfs(node,a):
  global answer,visited,border
  now = a[node]

  visited[node] = 1

  for i in border[node]:
    if not visited[i]:
      now += dfs(i,a)

  answer += abs(now)
  return now





a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]

print(solution(a,edges))
