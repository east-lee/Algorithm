def moving_robot(robot_num, cmd, loop_cnt):
  global robot_position, ground

  robot_y, robot_x, robot_direction_index = robot_position[robot_num]
  cnt = 0

  if cmd == 'L':
    while cnt < loop_cnt:
      robot_direction_index = robot_direction_index - 1 if robot_direction_index != 0 else 3
      cnt += 1

  elif cmd == 'R':
    while cnt < loop_cnt:
      robot_direction_index = robot_direction_index + 1 if robot_direction_index != 3 else 0
      cnt += 1

  else:
    while cnt < loop_cnt:

      ground[robot_y][robot_x] = 0
      robot_y += direction[robot_direction_index][0]
      robot_x += direction[robot_direction_index][1]

      if 0<=robot_x<M and 0<=robot_y<N:
        if ground[robot_y][robot_x] != 0: #다른로봇이있다면
          return f"Robot {robot_num + 1} crashes into robot {ground[robot_y][robot_x]}"
        else:
          ground[robot_y][robot_x] = robot_num + 1

      else:

        return f"Robot {robot_num + 1} crashes into the wall"
      cnt += 1

  robot_position[robot_num] = [robot_y, robot_x, robot_direction_index]
  return "OK"

def main():

  for robot_num, cmd, loop_cnt in command_list:
    result = moving_robot(robot_num,cmd,loop_cnt)
    if result == "OK":

      continue
    return result

  return "OK"



def get_data():
  M, N = map(int,input().split())
  robot_cnt, command_cnt = map(int,input().split())
  direction_index_c = ['E','S','W','N']
  command_list = []
  robot_position = []

  ground = [
    [0] * M  for _ in range(N)
  ]

  for i in range(robot_cnt):
    x, y, direction = map(str, input().split())
    x = int(x) - 1
    y = N - int(y)
    ground[y][x] = i+1
    direction_index = direction_index_c.index(direction)
    robot_position.append([y,x,direction_index])


  for _ in range(command_cnt):
    robot_num, cmd, working_cnt = map(str, input().split())
    robot_num = int(robot_num) - 1
    working_cnt = int(working_cnt)
    command_list.append([robot_num, cmd, working_cnt])

  return [N,M,robot_position, command_list, ground]


if __name__ == "__main__":
  N,M,robot_position, command_list, ground = get_data()
  direction = [
    [0,1], [1,0],[0,-1],[-1,0]
  ] # 동 남 서 북

  print(main())

