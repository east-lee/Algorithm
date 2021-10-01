import sys

sys.setrecursionlimit(10**9)

def dfs(start):
  global parent

  for i in node[start]:
    if parent[i] == 0:
      parent[i] = start
      dfs(i)


if __name__ == "__main__":
  N = int(input())
  node = [
    [] for _ in range(N+1)
  ]

  parent = [
    0 for _ in range(N+1)
  ]

  for _ in range(N-1):
    node_1, node_2 = map(int ,input().split())
    node[node_1].append(node_2)
    node[node_2].append(node_1)


  dfs(1)

  for i in range(2,N+1): print(parent[i])


