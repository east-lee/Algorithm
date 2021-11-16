def get_data():
  N, M = map(int, input().split())
  arr = []

  for _ in range(N):
    arr.append(input())

  return [N, M, arr]

if __name__ == "__main__":
  N, M, arr = get_data()
  char_list = ['A','C','G','T']
  char_list.sort()
  result = ""
  result_cnt = 0
  cnt = 0

  while cnt < M:
    min_cnt = 1000
    min_char = ""
    for k in range(4):
      check_char = char_list[k]
      check_cnt = 0
      for i in range(N):
        check_arr_char = arr[i][cnt]
        if check_char != check_arr_char:
          check_cnt += 1
      if min_cnt > check_cnt:
        min_char = check_char
        min_cnt = check_cnt
    result += min_char
    result_cnt += min_cnt
    cnt += 1

  print(result)
  print(result_cnt)







# def solution(k, s):
#   distance = 0
#
#   for i in range(N):
#     if arr[i][k] != s:
#       distance += 1
#
#   return distance
#
# def make_s(k=0, s="", dist=0):
#   global result_list, result_dist
#   if k == M:
#     if dist == result_dist:
#       result_list.append(s)
#     elif dist < result_dist:
#       result_dist = dist
#       result_list = [s]
#     return
#
#   for m in range(4):
#
#     distance = solution(k, char_list[m])
#
#     if distance + dist > result_dist:
#       continue
#     else:
#       make_s(k+1, s+char_list[m], dist + distance)
#
#
# if __name__ == "__main__":
#   N, M, arr = get_data()
#   char_list = ['T', 'A', 'G', 'C']
#   result_list = []
#   result_dist = 50 * 1000
#
#   make_s()
#   result_list.sort()
#   # print(result_list)
#   print(result_list[0])
#   print(result_dist)
