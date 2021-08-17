from collections import deque

def BFS():
  visited = [False for _ in range(101)]
  start = 1
  dq = deque()
  dq.append([start, 0])

  while dq:
    s, cnt = dq.popleft()
    if s == 100:
      return cnt
    elif visited[s]: continue

    visited[s] = True

    for i in range(1,7):
      if 0<s+i<=100:
        dq.append([game_board[s+i],cnt+1])

def get_data():
  # N : 사다리 / M : 뱀
  N, M = map(int, input().split())
  game_board = [i for i in range(101)]

  for repeat_cnt in [N, M]:
    for _ in range(repeat_cnt):
      s, e = map(int, input().split())
      game_board[s] = e

  return game_board

if __name__ == "__main__":
  game_board = get_data()
  print(BFS())
