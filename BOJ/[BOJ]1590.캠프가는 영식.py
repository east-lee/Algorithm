if __name__ == "__main__":
  N, T = map(int, input().split())
  result = 2**31

  for _ in range(N):
    start_time, interval, n = map(int, input().split())
    start_time_list = [start_time + interval*i for i in range(n)]
    last_start_time = start_time_list[-1]

    if last_start_time < T: continue

    for i in range(n-1):
      if start_time_list[i] == T:
        result = 0
        break
      if start_time_list[i] < T <= start_time_list[i+1]:
        result = min(result, start_time_list[i+1] - T)
        break

  print(result) if result < 2**31 else print(-1)