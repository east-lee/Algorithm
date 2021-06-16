def find_pos_num(i,j):
  visited = [0]*10
  return_list = []
  box_i, box_j = 0,0

  for x in range(3):
    start, end = x*3, x*3+2
    if start<=i<=end: box_i = start
    if start<=j<=end: box_j = start

  for k in range(9):
    visited[SUDOKU[i][k]] = 1
    visited[SUDOKU[k][j]] = 1
  for bi in range(box_i, box_i+3):
    for bj in range(box_j,box_j+3):
      visited[SUDOKU[bi][bj]] = 1

  for check in range(1,10):
    if visited[check] == 0: return_list.append(check)

  return return_list


def find_blank(i=0,j=0):
  global SUDOKU, printed

  if printed: return
  if i == N:
    printed = True
    for line in SUDOKU:
      line = list(map(str,line))
      print(' '.join(line))
    return

  next_i = i if j < N-1 else i+1
  next_j = j+1 if j<N-1 else 0


  if SUDOKU[i][j]:
    find_blank(next_i, next_j)
  else: #스도쿠의 해당 공간이 비어있다면
    pos_list = find_pos_num(i,j)
    if not pos_list: return
    for pos in pos_list:
      SUDOKU[i][j] = pos
      find_blank(next_i,next_j)
      SUDOKU[i][j] = 0

if __name__ == "__main__":
  N = 9
  SUDOKU = list(list(map(int,input().split())) for _ in range(N))
  printed = False
  find_blank()