if __name__ == "__main__":
  F, S, G, U, D = map(int,input().split())
  # 총 F층 // 강호의위치 s층 // 사무실의위치 G층 // U층위로 // D층 아래로
  MESSAGE = "use the stairs"
  DP = [MESSAGE] * (1000001)
  DP[S] = 0

  q = []
  new_q = []
  cnt = 0
  q.append(S)

  while q:
    p = q.pop()
    if p == G:
      break
    check_1 = False
    check_2 = False
    if p+U <= F:

      if DP[p+U] ==MESSAGE:
        DP[p+U] = DP[p] + 1
        check_1 = True
      if p+U+D <= F and type(DP[p+U+D])==int:
        DP[p+U] = min(DP[p+U], DP[p+U+D])
        check_1 = True
      if check_1:
        new_q.append(p + U)


    elif p-D >= 1:

      if DP[p-D] == MESSAGE:
        DP[p-D] = DP[p] + 1
        check_2 = True
      if p-D-U >= 1 and type(DP[p-D-U]) == int:
        DP[p-D] = min(DP[p-D],DP[p-D-U]+1)
        check_2 = True
      if check_2:
        new_q.append(p-D)

    if not q and new_q:
      q = new_q
      cnt += 1
      new_q = []

  print(DP[G])


