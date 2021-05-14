def solution():
  global result
  q = []
  q.append([0,0,0])
  new_q = []
  cnt = 0
  # check에 0이면 말처럼움직일경우 거기로 못감, 1이면 원숭이처럼움직이면 못 감
  check_horse = list([0]*W for _ in range(H))
  check_monkey = list([0]*W for _ in range(H))
  check_horse[0][0] = 1
  check_monkey[0][0] = 1


  while q:
    y,x,k = q.pop()
    # y,x에서 출발 // k가 K보다 작아야지 말처럼움직일 수있음
    if y==H-1 and x == W-1:
      result = cnt
      break
    if k < K:
      for m in range(8):
        next_y, next_x = y+moving_horse[m][0], x+moving_horse[m][1]
        if 0<=next_y<H and 0<=next_x<W and not check_horse[next_y][next_x] and arr[next_y][next_x] != 1:
          check_horse[next_y][next_x] = 1
          new_q.append([next_y,next_x,k+1])
    for u in range(4):
      next_y,next_x = y+moving_monkey[u][0], x + moving_monkey[u][1]
      if 0 <= next_y < H and 0 <= next_x < W and not check_monkey[next_y][next_x] and arr[next_y][next_x] != 1:
        check_monkey[next_y][next_x] = 1
        new_q.append([next_y, next_x, k])
    if not q and new_q:
      q = new_q
      new_q = []
      cnt += 1


if __name__ == "__main__":
  K = int(input())
  W, H = map(int,input().split())
  arr = list(list(map(int,input().split())) for _ in range(H))
  result = -1
  moving_horse = [[-2,1],[-1,2],[2,1],[1,2],[2,-1],[1,-2],[-1,-2],[-2,-1]]
  moving_monkey = [[-1,0],[1,0],[0,1],[0,-1]]

  solution()

  print(result)