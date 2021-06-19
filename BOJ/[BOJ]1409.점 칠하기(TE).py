import sys
sys.setrecursionlimit(3000)

def DFS(start_idx,cnt,k,first_idx,rotation_degree, path):
  global visited,max_cnt
  if start_idx >= 2*N:
    if cnt > max_cnt: max_cnt = cnt
    return

  start_point = start_point_list[start_idx]
  next_point = start_point + rotation_degree

  next_point = next_point if next_point < 360 else next_point - 360

  if not visited[start_point] and next_point in start_point_list and visited[next_point] == 0:
    next_index = start_point_list.index(next_point)
    if next_index < start_idx: next_index += N
    visited[start_point] = 1
    visited[next_point] = 1
    DFS(next_index + 1, cnt + 2, k, first_idx, rotation_degree, path+str(start_idx) + str(next_index))
    DFS(start_idx + 1, cnt, k, first_idx, rotation_degree, path + str(start_idx) + str(next_index))
    visited[next_point] = 0
    visited[start_point] = 0
  else:
    DFS(start_idx + 1, cnt,k,first_idx,rotation_degree,path)

def set_rotation_degree(start,end):
  start_point = start_point_list[start]
  end_point = start_point_list[end]
  rotation_degree = end_point - start_point

  return [start_point,end_point,rotation_degree]

def get_start_point():
  start_point_list = []

  for _ in range(N):
    start_point_list.append(int(input()))

  return start_point_list


if __name__ == "__main__":
  N = int(input())
  start_point_list = get_start_point()
  start_point_list *= 2


  visited = [0]*361
  max_cnt = 0

  for start_idx in range(N-1):
    for to_start_idx in range(start_idx+1,N):

      start_point, end_point, rotation_degree = set_rotation_degree(start_idx,to_start_idx) #처음 틀어질 수 있는 각도를 지정

      visited[start_point], visited[end_point] = 1, 1
      DFS(to_start_idx+1,2,2,start_idx,rotation_degree, str(start_idx) + str(to_start_idx))
      visited[start_point], visited[end_point] = 0, 0

  print(max_cnt)



