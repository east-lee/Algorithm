def check_string(string):
  global check

  if string in check.keys():
    return False
  check[string] = 1

  return True


def make_string(k=0,mid_result = ''):
  global visited,result

  if k == len(S):
    if check_string(mid_result): result += 1
    return

  for index in range(len(S)):
    if visited[index]: continue
    elif len(mid_result) == 0:
      visited[index] = 1
      make_string(k+1, mid_result + S[index])
      visited[index] = 0
    elif mid_result[-1] != S[index]:
      visited[index] = 1
      make_string(k+1,mid_result+S[index])
      visited[index] = 0


if __name__ == "__main__":
  S = list(input())
  check = {}
  visited = [0 for _ in range(len(S))]
  result = 0
  make_string()
  print(result)