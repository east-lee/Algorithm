def main():
  board_start = 0
  cnt = 0
  for start_point, end_point in water_pool:
    # print(start_point,board_start,cnt)
    board_start = max(board_start,start_point)
    if board_start >= end_point:
      continue
    board_end = board_start + L - 1
    while board_end < end_point-1:
      board_start = board_end + 1
      board_end = board_start + L - 1
      cnt += 1
    board_start = board_end + 1
    cnt += 1
  print(cnt)

if __name__ == "__main__":
  N, L = map(int,input().split())
  water_pool = []
  for _ in range(N):
    water_pool.append(list(map(int,input().split())))

  water_pool.sort(key=lambda x:x[0])

  main()