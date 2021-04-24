if __name__ == "__main__":
  N, D = map(int,input().split())
  min_road = []
  for _ in range(N):
    s,e,v = map(int,input().split())
    if s<0 or s>D or e<0 or e>D or v >= (e-s): continue
    min_road.append([s,e,v])

  distance = [i for i in range(D+1)]

  for i in range(D+1):
    if i > 0: distance[i] = min(distance[i],distance[i-1]+1)
    for s,e,v in min_road:
      if s == i and distance[e] > distance[s] + v:
        distance[e] = distance[s] + v
  print(distance[D])