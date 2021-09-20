def next_position(i, j, direction_idx):
  return [i + direction[direction_idx][0], j + direction[direction_idx][1]]


if __name__ == "__main__":
  r1, c1, r2, c2 = map(int, input().split())
  length = max([abs(r1), abs(r2), abs(c1), abs(c2)])
  max_length = length * 2 + 1

  new_r1, new_c1, new_r2, new_c2 = r1+length, c1+length, r2+length+1, c2+length+1

  arr = [
    [0] * (new_c2-new_c1) for _ in range(new_r2-new_r1)
  ]

  start_y, start_x  = (length for _ in range(2))

  # R / U / L  / D
  direction = [
    [0,1], [-1,0],[0,-1],[1,0]
  ]
  num = 1
  idx = 0
  loop_cnt = 1
  loop_cnt_check = 0

  if new_r1<=start_y<new_r2 and new_c1<=start_x<new_c2:
    arr[start_y-new_r1][start_x-new_c1] = num

  max_length_num = 0

  while num < (max_length**2):
    cnt = 0

    while cnt < loop_cnt and num < max_length**2:
      num += 1
      start_y, start_x = start_y + direction[idx][0], start_x + direction[idx][1]
      cnt += 1

      if new_r1<=start_y<new_r2 and new_c1<=start_x<new_c2:
        arr[start_y - new_r1][start_x-new_c1] = num
        max_length_num = max(max_length_num, num)

    loop_cnt_check += 1
    if loop_cnt_check == 2:
      loop_cnt_check = 0
      loop_cnt += 1

    idx = (idx+1)%4

  for i in range(len(arr)):
    for j in range(len(arr[0])):
      blank_cnt = len(str(max_length_num)) - len(str(arr[i][j]))
      print(" " * blank_cnt, end="")
      print(arr[i][j], end = " ")
    print()

