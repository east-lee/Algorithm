def find_seperate_point(last_idx = 0, result=[], cnt = 0):
  global seperate_point_list

  if cnt == 2:
    seperate_point_list.append(result)
    return

  for i in range(1,N):
    if last_idx >= i: continue
    find_seperate_point(i,result+[i],cnt+1)

if __name__ == "__main__":
  string_data = list(input())
  N = len(string_data)
  seperate_point_list = []
  result_list = []
  find_seperate_point()

  for a_point, b_point in seperate_point_list:
    word_1 = string_data[:a_point]
    word_2 = string_data[a_point:b_point]
    word_3 = string_data[b_point:]
    result_word = ''.join(word_1[::-1] + word_2[::-1] + word_3[::-1])
    result_list.append(result_word)

  result_list.sort()
  print(result_list[0])

