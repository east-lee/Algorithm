# from collections import deque

def main():
  INF = 10**7
  result = [INF] * (n+1)
  result[c] = 0
  # q = deque()
  q = []
  new_q = []
  q.append(c)
  while q:
    start = q.pop()
    for end, time in connection[start]:
      if result[start]+time < result[end]:
        result[end] = result[start] + time
        new_q.append(end)
    if not q and new_q:
      q= new_q
      new_q =[]

  cnt = 0
  t = 0
  for i in result:
    if i != INF:
      if i > t: t = i
      cnt += 1
  print(cnt, t)



if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    n, d, c = map(int,input().split())
    computer = [0 for _ in range(n+1)]

    connection = [[] for _ in range(n+1)]
    for _ in range(d):
      a,b,s = map(int,input().split())
      connection[b].append([a,s])

    main()