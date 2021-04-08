M,N = map(int,input().split())

check = [False for _ in range(N+1)]
prime = []
for i in range(1,N+1):
  if i == 1:
    continue
  if not check[i]:
    x = i+i
    while x <= N:
      check[x] = True
      x += i
    if i >= M:
      prime.append(i)
for i in prime:print(i)
