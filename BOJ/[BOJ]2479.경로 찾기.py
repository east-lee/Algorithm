from collections import deque

def HAMING_LENGTH(A,B):
  global check_length

  if check_length[A][B] != -1:
    return check_length[A][B]

  cnt = 0

  for i in range(K):
    if code_list[A][i] != code_list[B][i]:
      cnt += 1
    if cnt >= 2:
      check_length[A][B] = 2
      check_length[B][A] = 2
      return check_length[A][B]

  check_length[A][B] = cnt
  check_length[B][A] = cnt

  return cnt


def main():
  visited = [0] * (N)
  visited[A] = 1
  q = deque()
  q.append([A,[A]])

  while q:
    start_point, path = q.popleft()
    if start_point == B:
      return path
    for i in range(N):
      if visited[i]: continue
      check = HAMING_LENGTH(start_point, i)
      if check == 1:
        q.append([i,path+[i]])
        visited[i] = 1

  return -1



def get_data():
  N, K = map(int,input().split())

  code_list = []

  for _ in range(N):
    new_code = input()
    code_list.append(new_code)

  A, B = map(int, input().split())

  return [N, K, code_list, A - 1 , B - 1]

if __name__ == "__main__":
  N, K, code_list, A, B = get_data()
  check_length = [
    [-1] * N for _ in range(N)
  ]
  result = main()

  if result == -1: print(result)
  else:
    for r in result:
      print(r+1,end=' ')