def get_data():
  H, W = map(int, input().split())
  info = list(
    map(int, input().split())
  )

  arr = [
    [0] * W for _ in range(H)
  ]

  for i in range(W):
    for j in range(info[i]):
      arr[H-1-j][i]= 1


  return [H, W, arr]


if __name__ == "__main__":
  H, W, arr = get_data()
  result = 0

  for i in range(H):
    cnt = 0
    left_block = False
    for j in range(W):
      if not left_block and arr[i][j] == 1:
        left_block = True
        cnt = 0
      elif left_block and arr[i][j] == 1:
        result += cnt
        cnt = 0
      elif not arr[i][j]: cnt += 1
  print(result)
