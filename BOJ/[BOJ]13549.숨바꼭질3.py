from collections import deque

if __name__ == "__main__":
  N, K = map(int, input().split())
  INF = 100001
  field = [False] * INF

  q = deque()
  q.append((N,0))
  field[N] = True

  while q:
    x, dist = q.popleft()
    if x == K:
      print(dist)
      break
    if x * 2 < INF and not field[x*2]:
      q.appendleft((2*x, dist))
      field[2*x] = True

    if x + 1 < INF and not field[x + 1]:
      q.append((x+1,dist+1))
      field[x+1] = True
    if x - 1 >= 0 and not field[x - 1]:
      q.append((x - 1, dist + 1))
      field[x - 1] = True