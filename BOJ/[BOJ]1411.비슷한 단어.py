def main():
  arr = []
  for _ in range(N): arr.append(input())
  cnt = 0
  for i in range(N):
    word_1 = arr[i]
    for j in range(i+1,N):
      word_2 = arr[j]
      if len(word_1) != len(word_2): continue

      change_word = {}
      breaker = False
      for k in range(len(word_1)):
        if  word_2[k] in change_word.keys():
          if word_1[k] != change_word[word_2[k]]:
            breaker = True
            break
        else:
          if word_1[k] in change_word.values() :
            breaker = True
            break
          change_word[word_2[k]] = word_1[k]
      # print(change_word,word_1,word_2,breaker)
      if not breaker:
        # print(word_1,word_2)
        cnt += 1

  print(cnt)





if __name__ == "__main__":
  N =int(input())
  main()