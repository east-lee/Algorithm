if __name__ == "__main__":
  N, L, R = map(int,input().split())
  arr = list(list(map(int,input().split())) for _ in range(N))
  Direction = [[1,0],[0,1],[-1,0],[0,-1]]
  result = 0
  while True:
    check = list([0]*N for _ in range(N))
    cnt = -1
    total_cnt = 0

    group_arr = [[] for _ in range(N**2)]
    group_sum = [0]*(N**2)

    for i in range(N):
      for j in range(N):
        if not check[i][j]:
          cnt += 1
          group_sum[cnt] += arr[i][j]
          group_arr[cnt].append([i,j])
          check[i][j] = 1
          q = [[i,j]]
          while q:
            ni ,nj = q.pop()
            for k in range(4):
              y,x = ni+Direction[k][0], nj+Direction[k][1]
              if 0<=y<N and 0<=x<N and not check[y][x] and L<= abs(arr[ni][nj]-arr[y][x])<=R:
                check[y][x] = 1
                group_sum[cnt] += arr[y][x]
                group_arr[cnt].append([y,x])
                q.append([y,x])

    if cnt == N**2-1: break
    result += 1

    for idx,i_arr in enumerate(group_arr):
      for j_arr in i_arr:
        y,x = j_arr
        arr[y][x] = group_sum[idx]//(len(i_arr))
    # print(result,'-------------')
    # for i in arr:
    #   print(i)
  print(result)



