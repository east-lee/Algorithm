def get_data():
  N = int(input())
  word_list = [
    input() for _ in range(N)
  ]

  return [N, word_list]

if __name__ == "__main__":
  N, word_list = get_data()
  result = 0

  word_list.sort(key = lambda x : len(x))

  for i in range(N):
    length_word_i = len(word_list[i])
    check = False
    for j in range(i+1, N):
      length_word_j = len(word_list[j])
      if word_list[j][:length_word_i] == word_list[i]:
        check = True
        break
    if not check: result += 1


  print(result)
