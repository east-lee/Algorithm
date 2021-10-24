import heapq

if __name__ == "__main__":
  N = int(input())
  heap = []

  for _ in range(N):
    num_list = list(map(int,input().split()))
    # print(num_list)
    if not heap:
      for num in num_list:
        heapq.heappush(heap, num)
    else:
      for num in num_list:
        if heap[0] < num:
          heapq.heappush(heap, num)
          heapq.heappop(heap)
  print(heap[0])
  # print(heap)