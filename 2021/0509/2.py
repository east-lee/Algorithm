def solution(places):
  answer = []

  for place in places:
    p_arr = []
    result = 1
    for i in range(5):
      for j in range(5):
        if place[i][j] == 'P':
          p_arr.append([i, j])
    for i in range(len(p_arr)):
      for j in range(len(p_arr)):
        if i == j: continue
        r1, c1 = p_arr[i]
        r2, c2 = p_arr[j]
        if abs(r1 - r2) + abs(c1 - c2) > 2:
          continue
        elif abs(r1 - r2) + abs(c1 - c2) == 1:
          result = 0
          break
        else:
          if r1 == r2:
            if place[r1][(c1 + c2) // 2] != 'X':
              result = 0
          elif c1 == c2:
            if place[(r1 + r2) // 2][c1] != 'X':
              result = 0
          else:
            if place[r1][c2] != 'X' or place[r2][c1] != 'X':
              result = 0
    answer.append(result)

  return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])