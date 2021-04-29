from collections import deque
from copy import deepcopy

def main():
  N_list = list(N)
  check = [[0]*1000001 for _ in range(11)]

  dq = deque()
  dq.append([0,N_list])
  result = -1
  while dq:
    k, arr = dq.popleft()
    if k == int(K):
      if int(''.join(arr)) > result: result = int(''.join(arr))
      continue

    for i in range(len(N)):
      for j in range(i+1,len(N)):
        new_arr = deepcopy(arr)
        new_arr[i],new_arr[j] = new_arr[j], new_arr[i]
        if new_arr[0] == '0':continue
        new_num = int(''.join(new_arr))
        if not check[k][new_num]:
          check[k][new_num] = 1
          dq.append([k+1,new_arr])
  return result


if __name__ == "__main__":
  N, K = map(str,input().split())
  print(main())