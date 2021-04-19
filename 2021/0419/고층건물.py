# 낮은건물에서도 위의 건물을 볼 수 있음

N = int(input())
buildings = list(map(int,input().split()))
check = [0]*N
for i in range(N):
  min_inclination = -99999999999
  for j in range(i+1,N):
    inclination = (buildings[j]-buildings[i])/(j-i)
    if min_inclination < inclination:
      min_inclination = inclination
      check[i] += 1
      check[j] += 1
print(max(check))
