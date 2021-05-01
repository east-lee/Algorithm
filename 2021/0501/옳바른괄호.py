def solution(inputString):
  answer = 0
  check_dict = {
    '(': 1, '{': 2, '[': 3, '<': 4,
    ')': -1, '}': -2, ']': -3, '>': -4
  }

  stack = []
  cnt = 0
  breaking = False
  for idx, i in enumerate(inputString):
    if i not in check_dict.keys(): continue

    now_num = check_dict[i]
    if now_num < 0:
      if not stack or stack[-1] + now_num != 0:
        breaking = True
        answer = -idx
        break
      else:
        cnt += 1
        stack.pop()
    else:
      stack.append(now_num)
  if stack:
    answer = -idx
  else:
    if not breaking:
      answer = cnt

  return answer