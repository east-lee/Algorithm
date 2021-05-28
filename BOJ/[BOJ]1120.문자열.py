def find_same_length(n,A):
  return_list = []

  for i in range(n+1):
    new_A = A[:]
    front_cnt = i
    back_cnt = (n-i)

    for _ in range(front_cnt):
      new_A.insert(0,'.')
    for _ in range(back_cnt):
      new_A.append('.')
    return_list.append(new_A)
  return return_list


def check(A,B):
  N = len(A)
  cnt = 0
  for i in range(N):
    if A[i] != B[i] and A[i] != '.':
      cnt += 1
    elif A[i] == '.':
      continue
  return cnt

if __name__ == "__main__":
  A,B = map(list,input().split())
  A_list = []
  if len(A) != len(B):
    A_list = find_same_length(len(B)-len(A),A)
  else:
    A_list = [A]

  min_result = 51
  for a in A_list:
    min_result = min(min_result,check(a,B))
  print(min_result)