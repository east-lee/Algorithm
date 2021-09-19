import heapq

def get_data():
  N = int(input())
  maze = list(
    list(map(int,list(input()))) for _ in range(N)
  )

  return [N, maze]


if __name__ == "__main__":
  N, maze = get_data()
  visited = [
    [False] * N for _ in range(N)
  ]
  direction = [
    [-1, 0], [0, 1], [1, 0], [0, -1]
  ]

  start_y, start_x = 0, 0

  q = []
  heapq.heappush(q, (0,start_y, start_x))
  visited[0][0] = True

  while q:
    broken_cnt , y, x = heapq.heappop(q)

    if y == x and y == N-1:
      print(broken_cnt)
      break

    for k in range(4):
      next_y, next_x = y + direction[k][0], x + direction[k][1]

      if 0<=next_y<N and 0<=next_x<N and not visited[next_y][next_x]:
        visited[next_y][next_x] = True
        if maze[next_y][next_x] == 0:
          maze[next_y][next_x] = 1
          heapq.heappush(q, (broken_cnt+1,next_y, next_x))
        else:
          heapq.heappush(q, (broken_cnt, next_y, next_x))

