import sys
from collections import deque


def main():
  global min_result
  for combi in linked_combi:
    for nums in order:
      result = 0
      for idx,num in enumerate(nums):
        y,x = combi[idx][0], combi[idx][1]
        result += min_route_list[num][y][x]
      min_result = min(min_result,result)




def find_min_route(n,target):
  global min_route_list
  q = deque()
  q.append(target+[0])
  min_route_list[n][target[0]][target[1]] = 0
  while q:
    i,j,cnt = q.popleft()
    for k in range(4):
      y,x = i+direction[k][0], j+direction[k][1]
      if 0<=y<5 and 0<=x<5 and min_route_list[n][y][x] > cnt+1:
        min_route_list[n][y][x] = cnt+1
        q.append([y,x,cnt+1])

def find_linked_combi(k,n,last_idx,result_list):
  global linked_combi
  if k == n:
    if linked_check(result_list,n):
      linked_combi.append(result_list)
    return

  for i in range(5):
    if i < last_idx[0]: continue
    for j in range(5):
      if i == last_idx[0] and j <= last_idx[1]:
        continue
      next_list = result_list[:]
      next_list.append([i,j])
      find_linked_combi(k+1,n,[i,j],next_list)


def linked_check(arr,n):
  q = []
  q.append(arr[0])
  visited = [0]*n
  visited[0] = 1
  while q:
    y,x = q.pop()
    for k in range(4):
      i, j = y+direction[k][0], x+direction[k][1]
      if 0<=i<5 and 0<=j<5 and [i,j] in arr and visited[arr.index([i,j])] == 0:
        visited[arr.index([i,j])] = 1
        q.append([i,j])
  if visited == [1]*n:
    return True
  return False

def find_order(n,result):
  global order
  if len(result) == n:
    order.append(result)
    return

  for i in range(n):
    if i not in result:
      find_order(n,result+[i])





if __name__ == "__main__":
  DATA = list(list(input()) for _ in range(5))
  INF = sys.maxsize
  min_result = sys.maxsize
  target_list = []
  linked_combi = []
  order = []
  direction = [[-1,0],[1,0],[0,-1],[0,1]]

  # 조각상 위치 저장
  for i in range(5):
    for j in range(5):
      if DATA[i][j] == '*':
        target_list.append([i,j])

  #각각의 조각상이 각 위치에 갈때의 최단거리

  min_route_list = [[[INF]* 5 for _ in range(5)] for _ in range(len(target_list))]

  for n in range(len(target_list)):
    find_min_route(n,target_list[n])

  find_linked_combi(0,len(target_list),[-1,-1],[])
  find_order(len(target_list),[])
  main()

  print(min_result)


