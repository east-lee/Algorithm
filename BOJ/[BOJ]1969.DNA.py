def get_data():
  N, M = map(int, input().split())
  arr = []

  for _ in range(N):
    arr.append(input())

  return [N, M, arr]

def solution(k, s):
  distance = 0

  for i in range(N):
    if arr[i][k] != s:
      distance += 1

  return distance

def make_s(k=0, s="", dist=0):
  global result_list, result_dist
  if k == M:
    if dist == result_dist:
      result_list.append(s)
    elif dist < result_dist:
      result_dist = dist
      result_list = [s]
    return

  for m in range(4):

    distance = solution(k, char_list[m])

    if distance + dist > result_dist:
      continue
    else:
      make_s(k+1, s+char_list[m], dist + distance)


if __name__ == "__main__":
  N, M, arr = get_data()
  char_list = ['T', 'A', 'G', 'C']
  result_list = []
  result_dist = 50 * 1000

  make_s()
  result_list.sort()
  # print(result_list)
  print(result_list[0])
  print(result_dist)
