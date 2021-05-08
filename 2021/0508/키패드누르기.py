def solution(numbers,hand):
  answer = ''
  left_finger = {'1':True,'4':True,'7':True}
  right_finger = {'3':True,'6':True,'9':True}

  nums_arr = [
    [3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]
  ]

  left_hand = [3,0]
  right_hand = [3,2]

  for number in numbers:
    str_number = str(number)
    if str_number in left_finger.keys():
      left_hand = nums_arr[number]
      answer +='L'
    elif str_number in right_finger.keys():
      right_hand = nums_arr[number]
      answer += 'R'
    else:
      nums_position = nums_arr[number]
      left_lenght = abs(nums_position[0]-left_hand[0]) + abs(nums_position[1]-left_hand[1])
      right_length = abs(nums_position[0]-right_hand[0]) + abs(nums_position[1]-right_hand[1])
      if (left_lenght < right_length) or (left_lenght == right_length and hand =='left'):
        answer +='L'
        left_hand = nums_position
      elif (left_lenght > right_length) or (left_lenght==right_length and hand == 'right'):
        answer += 'R'
        right_hand = nums_position

  return answer






