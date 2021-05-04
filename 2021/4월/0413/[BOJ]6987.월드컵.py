def solution(game):
  arr = []
  for i in range(6):
    arr.append(game[3*i:3*i+3])
  cnt = 0
  for team in arr:
    for i in range(3):
      if team[i]:
        arr = matching(cnt,i,team[i],arr)
        if arr==-1:
          return '0 '
  return '1 '

def matching(idx,i,loop_cnt,arr):
  if i == 0: j = 2
  elif i ==2: j = 0
  else:j=1
  cnt = 0
  remove_cnt = 0
  while cnt < loop_cnt:
    for k in range(6):
      if k != idx and arr[k][j] > 0:
        arr[k][j] -= 1
        arr[idx][i] -= 1
        remove_cnt += 1
        break
    cnt += 1
    if remove_cnt != cnt : return -1
  return arr


if __name__ == "__main__":
  match =  list(list(map(int,input().split())) for _ in range(4))
  result = ''
  for game in match:
    result += solution(game)
  print(result)