def DFS(check_result, i,j,k):
  global pos_num_list
  if k == 5:
    pos_num_list.append(check_result)
    return

  for m in range(4):
    y,x = i+direction[m][0], j+direction[m][1]
    if 0<=y<5 and 0<=x<5:
      DFS(check_result+number_board[y][x],y,x,k+1)


if __name__ == "__main__":
  number_board = list(list(map(str,input().split())) for _ in range(5))
  pos_num_list = []
  direction = [[-1,0],[1,0],[0,-1],[0,1]]
  for i in range(5):
    for j in range(5):
      DFS(number_board[i][j], i, j, 0)

  result = list(set(pos_num_list))
  print(len(result))