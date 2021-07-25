
def DFS(k = 0, before_num = -1, bbefore_num = -2):
  global bead, cnt

  if k == total_bead_cnt:
    cnt += 1
    return

  for i in range(N):
    if i == before_num or i == bbefore_num or bead[i] == 0:
      continue

    bead[i] -= 1
    DFS(k+1, i, before_num)
    bead[i] += 1


def get_data():
  N = int(input())
  bead = []

  for _ in range(N):
    bead.append(int(input()))

  return [N, bead]


if __name__ == "__main__":
  N, bead = get_data()
  total_bead_cnt = sum(bead)
  cnt = 0
  DFS()

  print(cnt)