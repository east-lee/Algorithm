



def get_data():
  N = int(input())
  todo_list = [
    list(map(int,input().split())) for _ in range(N)
  ]

  todo_list.sort(key = lambda x: x[1], reverse = True)

  return [N, todo_list]

if __name__ == "__main__":
  N, todo_list = get_data()

  start_time = todo_list[0][1] - todo_list[0][0]

  for i in range(1,N):
    if start_time > todo_list[i][1]:
      start_time  = todo_list[i][1] - todo_list[i][0]
    else:
      start_time -= todo_list[i][0]

  start_time = start_time if start_time >= 0 else -1

  print(start_time)