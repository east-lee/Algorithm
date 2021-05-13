def solution(s):
  answer = []

  for string in s:
    stack = []
    cnt = 0
    for i in range(len(string)):
      stack.append(string[i])
      while len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
        for _ in range(3):
          stack.pop()
        cnt += 1

    answer_str = ''
    mid_str = ''
    cnt_1 = 0
    for i in stack:
      if i == '0':
        cnt_1 = 0
        answer_str += mid_str
        answer_str += '0'
        mid_str = ''
      else:
        cnt_1 += 1
        mid_str += '1'
      if cnt_1 == 3 and cnt:
        while cnt:
          answer_str += '110'
          cnt -= 1
        answer_str += mid_str
        mid_str = ''
        cnt_1 = 0

    for _ in range(cnt):
      answer_str += '110'
    answer_str += mid_str
    answer.append(answer_str)

  return answer