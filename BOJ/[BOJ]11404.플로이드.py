# 플로이드 - 와샬
# 98% => INF 처리 어떻게?


def main():
  global bus_info

  for k in range(N):
    for i in range(N):
      for j in range(N):
        if i != j and bus_info[i][j] > bus_info[i][k] + bus_info[k][j]:
          bus_info[i][j] = bus_info[i][k] + bus_info[k][j]


def get_data():
  N, M = [int(input()) for _ in range(2)]
  INF = 1000000

  bus_info = [
    [INF] * N for _ in range(N)
  ]

  for _ in range(M):
    start, end, cost = map(int,input().split())
    if bus_info[start-1][end-1] > cost:
      bus_info[start-1][end-1] = cost

  return [N, M, bus_info, INF]

if __name__ == "__main__":
  N, M, bus_info, INF = get_data()

  for i in range(N): bus_info[i][i] = 0

  main()

  for line in bus_info:
    for cost in line:
      r = 0
      if cost != INF:
        r = cost
      print(cost,end = " ")
    print()

