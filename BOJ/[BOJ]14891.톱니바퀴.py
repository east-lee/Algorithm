from collections import deque

def gear_rotation(direction_num, rotate_idx):
  global gear_list

  if direction_num == 1:
    gear_list[rotate_idx] = [gear_list[rotate_idx][-1]]+ gear_list[rotate_idx][:-1]
  else:
    gear_list[rotate_idx] = gear_list[rotate_idx][1:] + [gear_list[rotate_idx][0]]

  return


def get_data():
  N = 4
  gear_list = [
    list(map(int,list(input()))) for _ in range(N)
  ]

  cmd_length = int(input())

  cmd = [list(map(int,input().split())) for _ in range(cmd_length)]

  return [N, gear_list, cmd_length , cmd]


if __name__ == "__main__":
  N, gear_list, cmd_length ,cmd = get_data()

  for rotate_gear_index, direction in cmd:
    rotate_gear_index -= 1
    rotation_list = []
    linked_check = [0]*(N-1)

    for k in range(3):
      if gear_list[k][2] != gear_list[k+1][6]:
        linked_check[k] = 1

    dq = deque()
    dq.append(rotate_gear_index)
    visited = [0] * N
    while dq:
      x = dq.popleft()
      if visited[x]: continue
      visited[x] = 1
      rotation_list.append(x)

      for m in [-1,1]:
        next_x = x + m
        if 0<=next_x<N and linked_check[min(x, next_x)]:
          dq.append(next_x)
    # print(rotation_list)
    for rotate_idx in rotation_list:
      direction_num = direction if rotate_gear_index % 2 == rotate_idx % 2 else -direction
      gear_rotation(direction_num, rotate_idx)

    # print("________________________")
    # for line in gear_list: print(line)
  #

  result = 0
  for i in range(4):
    # print(gear_list[i][0])
    if gear_list[i][0]== 1:
      result += 2**i
  print(result)
