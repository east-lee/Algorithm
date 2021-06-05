def DFS(y=15, x=15, percentage = 1, k = 0):
  global route_check_list, result

  if k == N:
    # print('--------------------------------------')
    # for i in route_check_list:
    #   print(i)
    result += percentage
    return

  for m in range(4):
    percentage_m = percentage_list[m] / 100
    i, j = y+direction[m][0], x+direction[m][1]
    if route_check_list[i][j] == 0:
      route_check_list[i][j] = 1
      DFS(i,j,percentage*percentage_m,k+1)
      route_check_list[i][j] = 0

if __name__ == "__main__":
  N, p1, p2, p3, p4 = map(int,input().split())
  direction = [[0,1],[0,-1],[1,0],[-1,0]] #동서남북
  percentage_list = [p1,p2,p3,p4] #동서남북
  route_check_list = list([0]*30 for _ in range(30))
  route_check_list[15][15] = 1
  result = 0
  DFS()
  print(result)