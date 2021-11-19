from queue import PriorityQueue

def solution():
  pq = PriorityQueue()
  pq.put((-arr[0][1], arr[0][1]))
  for i in range(1,N):
    if pq.queue[-1][-1] <= arr[i][0]:
      pq.get()
      pq.put((-arr[i][1], arr[i][1]))
    else:
      pq.put((-arr[i][1], arr[i][1]))

  print(pq.qsize())
  return
def get_data():
  N = int(input())
  arr = []

  for _ in range(N):
    start_time, end_time = map(int,input().split())
    arr.append([start_time, end_time])

  arr.sort(key=lambda x:x[0])

  return [N, arr]

if __name__ == "__main__":
  N, arr = get_data()
  solution()