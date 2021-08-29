def search_word(k, i, j):
  global visited, word_list

  word = puzzle[i][j]
  visited[k][i][j] = True
  y, x = i, j
  while True:
    y, x = y+direction[k][0], x+direction[k][1]
    if 0<=y<R and 0<=x<C and puzzle[y][x] != "#":
      visited[k][y][x] = True
      word += puzzle[y][x]
    else: break

  if len(word) > 1: word_list.append(word)



def get_data():
  R, C = map(int, input().split())
  puzzle = list(
    list(input()) for _ in range(R)
  )

  return [R, C, puzzle]


if __name__ == "__main__":
  R, C, puzzle = get_data()
  word_list = []
  visited = [[
    [False] * C for _ in range(R)
  ] for _ in range(2)]

  direction = [
    [0,1], [1,0]
  ]

  for i in range(R):
    for j in range(C):
      if puzzle[i][j] == "#": continue

      for k in range(2):
        if visited[k][i][j] == False:
          search_word(k,i,j)

  word_list.sort()

  print(word_list[0])