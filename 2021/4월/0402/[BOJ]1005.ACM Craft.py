def solution():
  visited = [0]*(N+1)
  visited[W] = 1
  total_time = time[W]
  q = []
  q.append(W)

  while q:
    p = q.pop()
    #print(p)
    before_p = to_do[p]
    if not before_p: continue
    max_time = []
    for i in before_p:
      if visited[i]:
        continue
      q.append(i)
      visited[i] = 1
      max_time.append(time[i])
    # print(total_time, max_time)
    if max_time:
      total_time += max(max_time)

  print(total_time)





if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    N, K = map(int,input().split())
    time = list(map(int,input().split()))
    time.insert(0,0)

    to_do = list([] for _ in range(N+1))
    for _ in range(K):
      before_i, after_i = map(int,input().split())
      to_do[after_i].append(before_i)

    W = int(input())
    solution()

