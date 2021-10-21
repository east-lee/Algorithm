def spring():
  # 자신의 나이만큼 양분을 먹는다. 나이가 어린순으로
  global tree, A, dead_tree

  for i in range(N):
    for j in range(N):
      if tree[i][j] == []: continue
      tree[i][j].sort()
      dead_cnt = 0
      for tree_idx in range(len(tree[i][j])):
        if A[i][j] < tree[i][j][tree_idx]:
          dead_cnt += 1
          dead_tree[i][j].append(tree[i][j][tree_idx])
        else:
          A[i][j] -= tree[i][j][tree_idx]
          tree[i][j][tree_idx] += 1

      for _ in range(dead_cnt):
        tree[i][j].pop()


def summer():
  global A
  for i in range(N):
    for j in range(N):
      if not dead_tree[i][j]: continue

      for dead_age in dead_tree[i][j]:
        A[i][j] += dead_age//2

def autumn():
  global tree

  for i in range(N):
    for j in range(N):

      for t in tree[i][j]:
        if t > 0 and t % 5 == 0:
          for k in range(8):
            y, x = i + direction[k][0], j + direction[k][1]
            if 0<=y<N and 0<=x<N:
              tree[y][x].append(1)

def winter():
  global A

  for i in range(N):
    for j in range(N):
      A[i][j] += B[i][j]

def get_data():
  N, M, K = map(int, input().split())
  A = list([5]*N for _ in range(N))
  B = list(list(map(int,input().split())) for _ in range(N))
  tree = [[[] for _ in range(N)] for _ in range(N)]
  # print(tree)
  for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

  return [N, M, K, A, B, tree]
if __name__ == "__main__":
  N, M, K, A, B, tree = get_data()
  direction = [
    [-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1,-1],[1,0], [1,1]
  ]

  for _ in range(K):
    dead_tree = [[[] for _ in range(N)] for _ in range(N)]

    spring()
    summer()
    autumn()
    winter()

  result = 0

  for i in range(N):
    for j in range(N):
      result += len(tree[i][j])

  print(result)
