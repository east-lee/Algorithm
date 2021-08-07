from collections import deque

def get_data():
  N, T = map(int, input().split())
  arr = [
    [] for _ in range(T+1)
  ]

  for _ in range(N):
    x, y = map(int, input().split())
    if x not in arr[y]: arr[y].append(x)

  return [N, T, arr]


if __name__ == "__main__":
  N, T, arr = get_data()
  dq = deque()
  dq.append([0,0,0])
  result = -1

  while dq:
    x, y, dist = dq.popleft()
    if y == T:
      result = dist
      break

    for ny in range(y-2, y+3):
      if 0<=ny<=T:
        for nx in range(x-2,x+3):
          if nx in arr[ny]:
            arr[ny].remove(nx)
            dq.append([nx,ny,dist+1])

  print(result)