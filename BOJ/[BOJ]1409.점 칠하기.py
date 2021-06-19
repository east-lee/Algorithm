def main():
  global max_cnt

  for rotation in pos_rotation_list:
    visited = [0] * 360
    cnt = 0
    for start in range(2*N):
      start_point = point_list[start]
      next_point = start_point + rotation
      if next_point >= 360: next_point -= 360

      if visited[start_point] or visited[next_point]:
        continue

      if point_check_list[next_point]:
        cnt += 2
        visited[start_point] = 1
        visited[next_point] = 1
    max_cnt = max(max_cnt,cnt)


def get_pos_rotation_degree(start,end):
  start_point = point_list[start]
  end_point = point_list[end]

  rotation_degree = end_point - start_point

  return rotation_degree


def get_start_point():
  global point_check_list

  start_point_list = []

  for _ in range(N):
    n = int(input())
    start_point_list.append(n)
    point_check_list[n] = 1

  return start_point_list

if __name__ == "__main__":
  N = int(input())
  point_check_list = [0] * 360
  point_list = get_start_point()

  max_cnt = 0

  point_list *= 2 # 360도를 넘을 경우를 대비하여 2배로 늘림

  pos_rotation_list = []

  for i in range(N-1):
    for j in range(i+1,N):
      pos_rotation = get_pos_rotation_degree(i,j)
      pos_rotation_list.append(pos_rotation)

  pos_rotation_list = list(set(pos_rotation_list))
  pos_rotation_list.sort()

  main()


  print(max_cnt)


