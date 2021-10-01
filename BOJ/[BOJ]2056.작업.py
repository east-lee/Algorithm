def get_data():
  N = int(input())
  working_time = [0] * (N+1)
  link = {}

  for i in range(1, N+1):
    working_info = list(map(int, input().split()))
    working_time[i] = working_info[0]
    if working_info[1] == 0:
      continue
    for j in working_info[2:]:
      if i not in link:
        link[i] = [j]
      else:
        link[i].append(j)

  return [N, working_time, link]


if __name__ == "__main__":
  N, working_time, link = get_data()

  for i in range(1, N+1):
    if i in link:
      t = 0
      for j in link[i]:
        t = max(t, working_time[j])
      working_time[i] += t
  # print(working_time)
  print(max(working_time))