def point_sorting():
  global point_list
  point_list.sort(key=lambda x:(x[0],x[1]))

def get_data():
  N = int(input())
  point_list = []

  for _ in range(N):
    x,y = map(int,input().split())
    point_list.append([x,y])

  return [N, point_list]


def main():
  for point in point_list:
    print(point[0],point[1])

if __name__ == "__main__":
  N, point_list = get_data()
  point_sorting()

  main()