def main(l,r):
  if l == r:
    print(l**2)
    return l
  elif abs(l-r) == 1:
    if checking(r):
      print(r**2)
    else: print(l**2)
    return

  x = (l+r)//2
  if checking(x):main(x,r)
  else:main(l,x)


def checking(x):
  possible = False
  for i in range(n - x + 1):
    for j in range(m - x + 1):
      check = True
      for ni in range(i, i + x):
        for nj in range(j, j + x):
          if arr[ni][nj] == "0":
            check = False
            break
        if not check: break
      if check:
        possible = True
        break
    if possible: break
  return possible



if __name__ == "__main__":
  n, m = map(int,input().split())
  arr = list(list(input()) for _ in range(n))
  L, R = 0, min(n,m)
  main(L,R)