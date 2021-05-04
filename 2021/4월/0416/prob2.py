
#2
def solution(s):
    answer = check(s)
    cnt = 0
    while cnt < len(s) - 1:
      s = s[1:] + s[0]
      answer += check(s)
      cnt += 1
    return answer


def check(arr):
  start = ['[', '{', '(']
  end = [']', '}', ')']
  stack = [
    [], [], []
  ]

  for i in arr:
    if i in start:
      stack[start.index(i)].append(i)
    else:
      if stack[end.index(i)]:
        stack[end.index(i)].pop()
      else:
        return 0
  if stack[0] or stack[1] or stack[2]: return 0
  return 1