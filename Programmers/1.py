def solution(s):
  answer = ''
  num_eng_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                  'nine': 9}

  num_eng = ''
  for i in s:
    try:
      i = int(i)
      num_eng += str(i)
    except:
      num_eng += str(i)

    if num_eng in num_eng_dict.keys():
      answer += str(num_eng_dict[num_eng])
      num_eng = ''
  print(answer)
  answer = int(answer)

  return answer

s ="123"
solution(s)