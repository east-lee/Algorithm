import heapq

def get_data():
  n = int(input())
  lecture_info = [
    list(map(int, input().split())) for _ in range(n)
  ]

  return [n, lecture_info]


if __name__ == "__main__":
  n, lecture_info = get_data()
  lecture_info.sort(key = lambda x:(x[1]))

  result = []
  #print(lecture_info)
  for price, day in lecture_info:
    heapq.heappush(result, price)
    if len(result) > day : heapq.heappop(result)
    #print(result)

  print(sum(result))