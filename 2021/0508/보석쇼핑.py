# # 효율성 0점
# def solution(gems):
#   answer = []
#
#   no_repeat_gems = list(set(gems))
#   min_length = len(no_repeat_gems)
#
#   for length in range(min_length, len(gems) + 1):
#     for start in range(len(gems) - length + 1):
#       check_gems = gems[start:start + length]
#       check_cnt = len(list(set(check_gems)))
#       if check_cnt == min_length:
#         answer = [start + 1, start + length]
#         break
#     if answer: break
#
#   return answer

# 시작점이 뒤에있는애들은 더짧을수도 있다..
from collections import deque


def solution(gems):
  answer = []

  no_repeat_gems = list(set(gems))
  min_length = len(no_repeat_gems)
  check_dict = {}
  for gem in no_repeat_gems:
    check_dict[gem] = 0

  dq = deque()
  check_idx = 0
  for gem in gems:
    dq.append(gem)
    check_dict[gem] += 1
    while dq and check_dict[dq[0]] >= 2:
      check_dict[dq[0]] -= 1
      dq.popleft()

      check_idx += 1
    breaker = False
    for i in check_dict.values():
      if i == 0:
        breaker = True
        break
    if not breaker:
      answer = [check_idx + 1, check_idx + len(dq)]
      break

  return answer
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])


def solution(gems):
  answer = []

  no_repeat_gems = list(set(gems))
  min_length = len(no_repeat_gems)
  check_dict = {}
  for gem in no_repeat_gems:
    check_dict[gem] = 0

  dq = []
  check_idx = 0
  for gem in gems:
    dq.append(gem)
    check_dict[gem] += 1
    while dq and check_dict[dq[check_idx]] >= 2:
      check_dict[dq[check_idx]] -= 1
      check_idx += 1
    breaker = False
    for i in check_dict.values():
      if i == 0:
        breaker = True
        break
    if not breaker and not answer:
      answer = [check_idx + 1, len(dq) - check_idx]
    elif not breaker and answer and (answer[1] - answer[0]) > (len(dq) - check_idx - check_idx - 1):
      answer = [check_idx + 1, len(dq) - check_idx
      if answer and (answer[1] - answer[0] + 1) == min_length:
        break

  return answer