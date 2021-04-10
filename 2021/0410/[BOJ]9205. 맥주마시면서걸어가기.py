def main():
  cnt = 0
  now = home
  result = 'happy'
  while cnt < n+2:
    if store:
      if abs(now[0]-festival[0]) + abs(now[1]-festival[1]) <= 1000:
        break
      end = store.pop()
    else: end = festival

    distance = abs(now[0]-end[0]) + abs(now[1]-end[1])
    if distance > 1000:
      result ='sad'
      break
    cnt += 1
    now = end
  return result

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    n = int(input()) #편의점 개수
    home = list(map(int,input().split()))
    store = []
    for _ in range(n):
      store.append(list(map(int,input().split())))
    festival = list(map(int,input().split()))
    store = store[::-1]
    print(main())
