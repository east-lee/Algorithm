def solution(data):
  arr = []
  for s in data:
    if s in check_dict.keys():
      if check_dict[s] < 0: arr.append(check_dict[s])
      else:
        if not arr or arr[-1] + check_dict[s] != 0: return 'no'
        arr.pop()
  if arr: return 'no'
  return 'yes'

check_dict = {'(':-1,'[':-2,']':2,')':1}

if __name__ == "__main__":
  while True:
    data = input()
    if data == '.':
      break
    print(solution(data))