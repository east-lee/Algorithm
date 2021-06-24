def check_paper(board):
  n = len(board)

  first_num = board[0][0]
  for i in range(n):
    for j in range(n):
      if first_num != board[i][j]:
        return False

  return True


def divide_board(board):
  n = len(board)
  n = n//3

  board_list = []
  for i in range(3):
    for j in range(3):
      copy_board = list([0]*n for _ in range(n))
      start_i, end_i, start_j, end_j = n*i, n*i+n, n*j, n*j+n
      s_i, s_j = 0, 0
      for m in range(start_i,end_i):
        for k in range(start_j, end_j):
          copy_board[s_i][s_j] = board[m][k]
          s_j += 1
        s_i += 1
        s_j = 0
      board_list.append(copy_board)
  return board_list


def main(board):
  global result_list
  check = check_paper(board)
  if check: #만약 체크 보드를 했는대 이게 하나의 종이로 표현이 된다면
    result_list[board[0][0]+1] += 1 #첫번째있는 숫자에서 +1 을 해서 (-1 => 0) 숫자를 더해준다
  else: # 그게 아니라면 이거를 나누고 각각의 나눈 것들을 다시 main(board) 로 넘겨준다!
    board_list = divide_board(board)
    for a_board in board_list:
      main(a_board)

def get_data():
  N = int(input())
  paper_board = list(
    list(map(int,input().split()))
    for _ in range(N)
  )

  return [N, paper_board]

if __name__ == "__main__":
  N, paper_board = get_data()
  result_list = [0 for _ in range(3)]
  main(paper_board)

  for result in result_list: print(result)