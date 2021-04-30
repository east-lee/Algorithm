from collections import deque
from copy import deepcopy

def main():
  dq = deque()
  dq.append([list(str(prime_1)),0])
  result = 'impossible'
  while dq:
    now_num_list,cnt = dq.popleft()
    if list_to_num(now_num_list) == prime_2:
      result = cnt
      break

    for i in range(4):
      for j in range(10):
        copy_list = deepcopy(now_num_list)
        copy_list[i] = str(j)
        if copy_list == now_num_list or copy_list[0] == '0' or prime[list_to_num(copy_list)] or visited[list_to_num(copy_list)]: continue
        visited[list_to_num(copy_list)] = 1
        dq.append([copy_list,cnt+1])
  return result

def list_to_num(arr):
  return int(''.join(arr))



def find_prime():
  arr = [0] * 10000
  arr[1] = 1
  for i in range(2,10000):
    if arr[i] == 0:
      x = 2*i
      while x < 10000:
        arr[x] = 1
        x += i
  return arr

if __name__ == "__main__":
  T = int(input())
  prime = find_prime()
  for _ in range(T):
    prime_1, prime_2 = map(int,input().split())
    visited = [0]*10001
    visited[prime_1] = 1
    print(main())