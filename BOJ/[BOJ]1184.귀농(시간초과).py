def check(arr_list):
  global result
  # print(arr_list)
  for i in range(len(arr_list)-1):
    for j in range(i+1,len(arr_list)):
      A, B = arr_list[i], arr_list[j]
      if A[0][0] - 1 == B[3][0] and A[0][1] - 1 == B[3][1]:
        result += 1
      elif A[1][0] - 1 == B[2][0] and A[1][1] + 1 == B[2][1]:
        result += 1
      elif A[2][0] + 1 == B[1][0] and A[2][1] - 1 == B[1][1]:
        result += 1
      elif A[3][0] + 1 == B[0][0] and A[3][1] + 1 == B[0][1]:
        result += 1

def find_ground_cost():
  global ground_cost
  for i in range(N):
    for j in range(N):
      for n in range(N):
        for n_j in range(N):
          y,x = i+n, j+n_j
          result = 0
          if 0<=y<N and 0<=x<N:
            for m in range(i,y+1):
              for u in range(j,x+1):
                result += ground[m][u]
          else: break

          ground_cost[result].append([[i,j],[i,x],[y,j],[y,x]])


if __name__ == "__main__":
  N = int(input())
  ground = list(list(map(int,input().split())) for _ in range(N))
  ground_cost = list([] for _ in range(1000*(N**2)))
  find_ground_cost()
  result = 0

  for i in ground_cost:
    if len(i) >= 2:
      check(i)
  print(result)