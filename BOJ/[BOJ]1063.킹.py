if __name__ == "__main__":
  moving = [
    [0,1],[0,-1],[-1,0],[1,0],[1,1],[1,-1],[-1,1],[-1,-1]
  ]
  moving_word = [
    'R','L','B','T','RT','LT','RB','LB'
  ]
  board = list([0]*8 for _ in range(8))
  king, stone, N = map(str,input().split())

  king_col = ord(king[0])-65
  king_row = int(king[1])-1
  stone_col = ord(stone[0]) - 65
  stone_row = int(stone[1]) - 1

  for _ in range(int(N)):
    moving_input = input()
    moving_idx = moving_word.index(moving_input)
    next_king_col = king_col + moving[moving_idx][1]
    next_king_row = king_row + moving[moving_idx][0]
    next_stone_col, next_stone_row = stone_col, stone_row
    if 0<=next_king_col<8 and 0<=next_king_row<8:
      if next_king_col == next_stone_col and next_king_row == next_stone_row:
        next_stone_col += moving[moving_idx][1]
        next_stone_row += moving[moving_idx][0]
        if 0<=next_stone_row<8 and 0<=next_stone_col<8:
          king_col, king_row, stone_col , stone_row = next_king_col, next_king_row, next_stone_col, next_stone_row
        else:
          continue
      else:
        king_col, king_row = next_king_col, next_king_row
    else:
      continue

  king_position = chr(65+king_col) + str(king_row+1)
  stone_position =chr(65+stone_col) + str(stone_row+1)
  print(king_position)
  print(stone_position)
