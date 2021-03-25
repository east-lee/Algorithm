def solution():
  A_B_distance = ((x1-x2)**2+(y1-y2)**2)**0.5
  if A_B_distance == 0 and r1 == r2:
    print(-1)
  elif A_B_distance == r1+r2 or max(r1,r2) == min(r1,r2)+A_B_distance:
    print(1)
  elif A_B_distance > r1+r2 or max(r1,r2)>min(r1,r2)+A_B_distance:
    print(0)
  else:
    print(2)


T = int(input())
for _ in range(T):
  x1,y1,r1,x2,y2,r2 = map(int,input().split())
  solution()