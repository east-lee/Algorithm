def sorting_11651(arr):
  return_arr = sorted(arr,key = lambda x:(x[1],x[0]))

  return return_arr

def get_data():
  N = int(input())
  point_list = []

  for _ in range(N):
    xi, yi = map(int,input().split())
    point_list.append([xi,yi])

  return [N,point_list]


if __name__ == "__main__":
  N, point_list = get_data()
  result = sorting_11651(point_list)

  for x, y in result:
    print(x,y)