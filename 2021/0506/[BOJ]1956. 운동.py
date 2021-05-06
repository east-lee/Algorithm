import sys

def main():
  global distance

  for k in range(1,V+1):
    for i in range(1,V+1):
      for j in range(1,V+1):
        distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

if __name__ == "__main__":
  V, E = map(int,input().split())
  INF = sys.maxsize
  distance = list( [INF]*(V+1) for _ in range(V+1))

  for _ in range(E):
    start,end,dist = map(int,input().split())
    distance[start][end] = dist

  main()

  result = INF
  for i in range(1,V+1):
    if distance[i][i] < result: result = distance[i][i]

  print(result if result != INF else -1)