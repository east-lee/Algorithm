def play_game(order):
  global result

  inning_cnt, player_idx, score = [0 for _ in range(3)]

  while inning_cnt < N:
    b1, b2, b3 = 0, 0, 0
    out_cnt = 0

    while out_cnt < 3:
      player_num = order[player_idx % 9]
      hitting = player_info[inning_cnt][player_num]

      if hitting == 0:
        out_cnt += 1
      elif hitting == 1:
        score += b3
        b1, b2, b3 = 1, b1, b2
      elif hitting == 2:
        score += (b2 + b3)
        b1, b2, b3 = 0, 1, b1
      elif hitting == 3:
        score += (b1 + b2 + b3)
        b1, b2, b3 = 0, 0, 1
      else:
        score += (1+b1+b2+b3)
        b1,b2,b3 = 0, 0, 0
      player_idx += 1
    inning_cnt += 1

  result = max(result, score)


def set_player_order(k=0):
  global visited, order
  if k == 9:
    play_game(order)
    return

  if k == 3:
    set_player_order(k+1)
  else:
    for i in range(1,9):
      if visited[i]: continue
      visited[i] = 1
      order[k] = i
      set_player_order(k+1)
      order[k] = 0
      visited[i] = 0

def get_data():
  N = int(input()) #이닝정보
  player_info = [
    list(map(int,input().split())) for _ in range(N)
  ]

  return [N, player_info]


if __name__ == "__main__":
  N, player_info = get_data()
  visited = [0] * 9
  order = [0] * 9
  result = 0
  set_player_order()
  print(result)