import heapq

def get_data():
  N = int(input())
  arr = []

  for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))

  return [N, arr]
if __name__ == "__main__":
  N, arr = get_data()
  arr.sort()

  q = []

  for deadline, noodle in arr:
    heapq.heappush(q,noodle)
    if deadline < len(q):
      heapq.heappop(q)
  print(sum(q))
