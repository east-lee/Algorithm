def get_data():
  N, M = map(int, input().split())
  lecture_time = list(map(int, input().split()))

  return [N, M, lecture_time]


if __name__ == "__main__":
  N, M, lecture_time = get_data()
  total_time = sum(lecture_time)
  left, right = total_time // M , total_time
  result = total_time
  while left <= right:
    mid = (left + right) // 2
    divid_cnt = 0
    sum_check = 0

    if mid < max(lecture_time):
      left = mid + 1
      continue

    for t in lecture_time:
      if sum_check + t <= mid:
        sum_check += t
      else:
        sum_check = t
        divid_cnt += 1

    if divid_cnt <= M - 1:
      right = mid - 1
      result = min(result, mid)
    else:
      left = mid + 1
  print(result)

