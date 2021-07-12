def main():
  global cost

  for i in range(M-1):
    from_bus, to_bus = bus_list[i], bus_list[i+1]
    cost += A[from_bus-1][to_bus-1]

def get_data():
  N, M = map(int, input().split())
  bus_list = list(map(int,input().split()))
  A = []

  for _ in range(N):
    arr = list(map(int,input().split()))
    A.append(arr)

  return [N, M, bus_list, A]

if __name__ == "__main__":
  N, M, bus_list, A = get_data()
  cost = 0
  main()
  print(cost)