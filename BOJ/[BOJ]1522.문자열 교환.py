def main():
  for x1, y1, x2, y2 in mosaic:
    for i in range(y1-1,y2):
      for j in range(x1-1,x2):
        picture[i][j] += 1
  return counting()

def counting():
  result = 0

  for i in range(100):
    for j in range(100):
      if picture[i][j] > M:
        result += 1
  return result

if __name__ == "__main__":
  N, M = map(int,input().split())
  mosaic = list()
  for _ in range(N):
    mosaic.append(list(map(int,input().split())))

  picture = list([0]*100 for _ in range(100))
  print(main())

