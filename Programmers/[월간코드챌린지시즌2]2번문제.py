def solution(numbers):
  answer = []
  for number in numbers:
    bin_num = list(str(bin(number)))[2:]
    if bin_num[-1] == '0':
      answer.append(number + 1)
    else:
      cnt = 0
      for i in bin_num[::-1]:
        if i == '1':
          cnt += 1
        else:
          break
      answer.append(number + 2 ** (cnt - 1))
  return answer