def DFS(my_room = 1, path = [1]):
  global visited

  if visited.count(0)==1:

    return path

  connection_room_list = []

  for i in range(1,N+1):
    if connection_room[my_room][i] == 1 and visited[i] == 0:
      connection_room_list.append(i)

  if connection_room_list:
    connection_room_list.sort()
    next_room = connection_room_list[0]
    visited[next_room] = 1
    return DFS(next_room,path + [next_room])
  else:
    return DFS(path[path.index(path[my_room])-1],path)


if __name__ == "__main__":
  N,M = map(int,input().split())

  connection_room = list([0]*(N+1) for _ in range(N+1))
  visited = [0]*(N+1)
  visited[1] = 1
  for _ in range(M):
    start, end = map(int,input().split())
    connection_room[start][end] = 1
    connection_room[end][start] = 1

  result_path = DFS()
  result_path = ' '.join(list(map(str,result_path)))
  print(result_path)


