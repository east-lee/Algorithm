def count(x,y,inclination):
  cnt = 1
  # print(x,y,inclination)
  if inclination < 0:
    for i in range(x,y):
      # if (i-x-1) == 0:print(x,y,i,'000000000')
      if (buildings[i]-buildings[x-1])/(i-x+1) < inclination:
        continue
      else:
        cnt = 0
  else:
    for i in range(x,y):
      if (buildings[y]-buildings[i])/(y-i) > inclination:
        continue
      else:
        cnt = 0
  return cnt


if __name__ == "__main__":
  N = int(input())
  buildings = list(map(int,input().split()))

  result = 0
  for i in range(N):
    cnt = 0
    for j in range(N):
      if i == j: continue
      elif i<j and buildings[i]>=buildings[j]:
        cnt += count(i+1,j,(buildings[j]-buildings[i])/(j-i))
      elif i>j and buildings[j] <= buildings[i]:
        cnt += count(j+1,i,(buildings[i]-buildings[j])/(i-j))
    if result < cnt: result = cnt
  print(result)