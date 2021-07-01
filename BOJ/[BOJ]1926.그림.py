def find_picture(i,j):
  global visited_canvas

  area = 1
  stack = []
  stack.append([i,j])
  visited_canvas[i][j] = True

  while stack:
    y, x = stack.pop()

    for k in range(4):
      ny, nx = y+directino[k][0], x+directino[k][1]

      if 0<=ny<N and 0<=nx<M and canvas[ny][nx] and not visited_canvas[ny][nx]:
        visited_canvas[ny][nx] = True
        stack.append([ny,nx])
        area += 1

  return area

def main():
  global max_area, picture_cnt

  for i in range(N):
    for j in range(M):
      if canvas[i][j] and not visited_canvas[i][j]:
        area = find_picture(i,j)
        max_area = max(max_area,area)
        picture_cnt += 1


def get_data():
  N, M = map(int,input().split())
  canvas = list(list(map(int,input().split())) for _ in range(N))
  visited_canvas = list([False]* M for _ in range(N))

  return [N, M, canvas, visited_canvas]

if __name__ == "__main__":
  N, M, canvas, visited_canvas = get_data()

  directino = [
    [-1,0],[1,0],[0,-1],[0,1]
  ]

  max_area, picture_cnt = 0, 0

  main()

  print(picture_cnt)
  print(max_area)
