def pos_moving(x):
  x1 = x - 1 if x - 1 >= 0 else 0
  x2 = x + 1 if x+1 <= 2*K else 2*K
  x3 = 2*x if 2*x <= 2*K else 2*K

  return [x1,x2,x3]


def main():
  visited = [0]*(2*K + 1)
  visited[N] = 1
  q = [N]
  new_q = []
  find_K = False
  time = 0
  pos_num = 0
  while q:
    x = q.pop()
    pos_list = pos_moving(x)

    if x == K:
      find_K = True

    for next_x in pos_list:
      if next_x == K:
        pos_num += 1
      if visited[next_x] == 0:
        visited[next_x] = 1
        new_q.append(next_x)
    if not q and new_q and not find_K:
      time += 1
      q = new_q
      new_q = []

  print(time)
  print(pos_num)

def get_location():
  N, K = map(int,input().split())

  return [N, K]


if __name__ == "__main__":
  N, K = get_location()
  if N == K:
    print(0)
    print(1)
  else:
    main()
